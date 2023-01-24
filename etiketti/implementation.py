"""Implementation API for labeling."""
import argparse
import datetime as dti
import pathlib
import shutil
import subprocess  # nosec B404
import uuid
import warnings
from typing import no_type_check

try:
    from liitos import APP_ALIAS as CREATOR_NAME, __version__ as CREATOR_VERSION  # type: ignore
except ModuleNotFoundError:
    CREATOR_NAME = 'liitos'
    CREATOR_VERSION = '42'

from etiketti.discover import (
    extract_author,
    extract_meta_parts,
    get_producer,
    hash_file,
    load_conventions,
    load_label_context,
)
from etiketti import (
    ENCODING,
    LOG_SEPARATOR,
    TS_FORMAT_PATCH,
    TS_FORMAT_PAYLOADS,
    TS_FORMAT_ISO,
    ContextType,
    ConventionsType,
    PathLike,
    log,
)

warnings.filterwarnings('ignore')


@no_type_check
def log_subprocess_output(pipe, prefix: str):
    for line in iter(pipe.readline, b''):  # b'\n'-separated lines
        cand = line.decode(encoding=ENCODING).rstrip()
        if cand.strip():
            log.info(f'{prefix}: %s', cand)


def camelize_first_two(dashed_key: str) -> str:
    """Transform kebab-key-input into KebabKey."""
    words = dashed_key.split('-')
    return f'{words[0].title()}{words[1].title()}'


@no_type_check
def timestamp_patch(create_date: str, modify_date: str, path: PathLike) -> None:
    """Let exiftool patch the time fields."""
    # on linux the below twisted c->m and m->c mappings gives the correct timestamps
    exiftool_command = f'exiftool "-CreateDate={create_date}" "-ModifyDate={modify_date}" {path}'
    log.info(LOG_SEPARATOR)
    log.info(f'{exiftool_command} ...')
    process = subprocess.Popen(
        exiftool_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True  # nosec B602
    )
    with process.stdout:
        log_subprocess_output(process.stdout, 'timestamp-patch')
    return_code = process.wait()
    if return_code < 0:
        log.error(f'==> Timestamp patch process ({exiftool_command}) was terminated by signal {-return_code}')
    else:
        log.info(f'==> Timestamp patch process ({exiftool_command}) returned {return_code}')
    log.info(LOG_SEPARATOR)


@no_type_check
def pdf_attributes(path: PathLike) -> None:
    """Let exiftool assess the attributes."""
    exiftool_command = f'exiftool {path}'
    log.info(f'{exiftool_command} ...')
    process = subprocess.Popen(
        exiftool_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True  # nosec B602
    )
    with process.stdout:
        log_subprocess_output(process.stdout, 'meta-state')
    return_code = process.wait()
    if return_code < 0:
        log.error(f'==> Meta-state process ({exiftool_command}) was terminated by signal {-return_code}')
    else:
        log.info(f'==> Meta-state process ({exiftool_command}) returned {return_code}')
    log.info(LOG_SEPARATOR)


@no_type_check
def pdf_info(path: PathLike) -> None:
    """Let pdfinfo assess some attributes."""
    pdfinfo_command = f'pdfinfo {path}'
    log.info(f'{pdfinfo_command} ...')
    process = subprocess.Popen(
        pdfinfo_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True  # nosec B602
    )
    with process.stdout:
        log_subprocess_output(process.stdout, 'pdf-info')
    return_code = process.wait()
    if return_code < 0:
        log.error(f'==> Pdfinfo process ({pdfinfo_command}) was terminated by signal {-return_code}')
    else:
        log.info(f'==> Pdfinfo process ({pdfinfo_command}) returned {return_code}')
    log.info(LOG_SEPARATOR)


@no_type_check
def cross_correlate(source: PathLike, conventions: ConventionsType, context: ContextType, target: PathLike) -> None:
    """Load information per conventions and mix with source to create target pdf."""
    from pikepdf import Pdf  # Workaround to avoid the start-up log of backend in version calls etc.

    source = pathlib.Path(source)
    target = pathlib.Path(target)
    backend_version = 'cf. pdf.Producer'  # backend_version  # 'putki 2023.1.1'
    log.info('Retrieving producer information:')
    log.info(LOG_SEPARATOR)
    producer_version = get_producer()
    creator_version = f'{CREATOR_NAME} {CREATOR_VERSION}'

    author = extract_author(conventions['approvals-yml-path'])
    title, subject, keywords = extract_meta_parts(conventions['metadata-yml-path'])
    dc_subject = subject
    dc_creator = [author]
    dc_title = title
    keywords = keywords
    hashes = {f'{camelize_first_two(k)}Hash': f'sha512:{hash_file(v)}' for k, v in conventions.items() if '-tex-' in k}
    for k, v in hashes.items():
        log.info(f'- {k :17s} -> {v}')

    label_prefix = context['label']['prefix']
    label_site_id = context['label']['site-id']
    label_action_id = context['label']['action-id']
    classification = 'Internal'
    content_bits = '0'
    enabled = 'true'
    method = 'Privileged'

    st = source.stat()
    c_time_patch = dti.datetime.fromtimestamp(st.st_ctime, tz=dti.timezone.utc).strftime(TS_FORMAT_PATCH)

    m_time_iso = dti.datetime.fromtimestamp(st.st_mtime, tz=dti.timezone.utc).strftime(TS_FORMAT_ISO)
    m_time_patch = dti.datetime.fromtimestamp(st.st_mtime, tz=dti.timezone.utc).strftime(TS_FORMAT_PATCH)

    make_unique = str(uuid.uuid4())

    with Pdf.open(source) as pdf:
        with pdf.open_metadata(set_pikepdf_as_editor=False) as m:
            m.load_from_docinfo(pdf.docinfo)
            m[f'{label_prefix}Enabled'] = enabled
            m[f'{label_prefix}SetDate'] = m_time_iso  # was iso
            m[f'{label_prefix}Method'] = method
            m[f'{label_prefix}Name'] = classification
            m[f'{label_prefix}SiteId'] = label_site_id
            m[f'{label_prefix}ActionId'] = label_action_id
            m[f'{label_prefix}ContentBits'] = content_bits
            m['Classification'] = classification
            m['UniqueIdentity'] = make_unique
            m['xmp:CreateDate'] = c_time_patch  # was iso
            m['xmp:ModifyDate'] = m_time_patch  # was iso
            m['xmp:CreatorTool'] = creator_version
            m['pdf:Producer'] = producer_version
            m['dc:subject'] = dc_subject
            m['dc:title'] = dc_title
            m['dc:creator'] = dc_creator
            # m['dc:source'] = dc_source
            # m['SourceHash'] = source_hash
            for k, v in hashes.items():
                m[k] = v
            pdf.docinfo[f'/{label_prefix}Enabled'] = m[f'{label_prefix}Enabled']
            pdf.docinfo[f'/{label_prefix}SetDate'] = m[f'{label_prefix}SetDate']
            pdf.docinfo[f'/{label_prefix}Method'] = m[f'{label_prefix}Method']
            pdf.docinfo[f'/{label_prefix}Name'] = m[f'{label_prefix}Name']
            pdf.docinfo[f'/{label_prefix}SiteId'] = m[f'{label_prefix}SiteId']
            pdf.docinfo[f'/{label_prefix}ActionId'] = m[f'{label_prefix}ActionId']
            pdf.docinfo[f'/{label_prefix}ContentBits'] = m[f'{label_prefix}ContentBits']
            pdf.docinfo['/Classification'] = m['Classification']
            pdf.docinfo['/UniqueIdentity'] = m['UniqueIdentity']
            # pdf.docinfo['/Source'] = m['dc:source']
            # pdf.docinfo['/SourceHash'] = m['SourceHash']
            for k, v in hashes.items():
                pdf.docinfo[f'/{k}'] = v
            pdf.docinfo['/Author'] = m['dc:creator'][0]
            pdf.docinfo['/CreationDate'] = m['xmp:CreateDate']
            pdf.docinfo['/Creator'] = m['xmp:CreatorTool']
            pdf.docinfo['/Producer'] = m['pdf:Producer']
            pdf.docinfo['/Keywords'] = keywords
            pdf.docinfo['/ModDate'] = m['xmp:ModifyDate']
            pdf.docinfo['/PTEX.FullBanner'] = backend_version
            pdf.docinfo['/Subject'] = m['dc:subject']
            pdf.docinfo['/Title'] = m['dc:title']
            pdf.save(target, fix_metadata_version=False)

    log.info(LOG_SEPARATOR)
    log.info('Patching the timestamps:')
    timestamp_patch(create_date=m_time_patch, modify_date=c_time_patch, path=target)


def patch(options: argparse.Namespace) -> int:
    """Patch the two related meta structures of the pdf file"""
    in_pdf = pathlib.Path(options.in_pdf)
    out_pdf = pathlib.Path(options.out_pdf)
    cfg_path = pathlib.Path(options.cfg_path)
    enforce = options.enforce
    log.info(f'Patching pdf meta data of {in_pdf}')
    log.info(f'Configuration path is {cfg_path}')
    log.info(f'Output path is {out_pdf}')
    if enforce:
        log.warning(f'Labeling will be enforced by overwriting {in_pdf}')
    else:
        log.info(f'Labeling will NOT be enforced - {in_pdf} will not be modified')

    start_time = dti.datetime.now(tz=dti.timezone.utc)
    start_ts = start_time.strftime(TS_FORMAT_PAYLOADS)
    log.info(f'Start timestamp ({start_ts})')

    log.info(LOG_SEPARATOR)
    context = load_label_context(cfg_path)
    log.info('loaded label context:')
    for k, v in context['label'].items():
        log.info(f'- {k :17s} -> {v}')
    log.info(LOG_SEPARATOR)

    conventions = load_conventions(context, in_pdf)
    log.info('identified conventions:')
    for k, v in conventions.items():
        log.info(f'- {k :17s} -> {v}')
    log.info(LOG_SEPARATOR)

    log.info(LOG_SEPARATOR)
    log.info('PDF information from source file:')
    log.info(LOG_SEPARATOR)
    pdf_info(in_pdf)
    log.info('PDF attributes/labels from source file:')
    log.info(LOG_SEPARATOR)
    pdf_attributes(in_pdf)
    cross_correlate(source=in_pdf, conventions=conventions, context=context, target=out_pdf)
    log.info('PDF attributes/labels from target file:')
    log.info(LOG_SEPARATOR)
    pdf_attributes(out_pdf)
    log.info('PDF information from target file:')
    log.info(LOG_SEPARATOR)
    pdf_info(out_pdf)

    if enforce:
        log.warning(f'Enforcing labels by overwriting {in_pdf}')
        shutil.copy2(out_pdf, in_pdf)
        log.info(f'- {out_pdf} -> {in_pdf}')

    end_time = dti.datetime.now(tz=dti.timezone.utc)
    end_ts = end_time.strftime(TS_FORMAT_PAYLOADS)
    duration_secs = (end_time - start_time).total_seconds()
    log.info(f'End timestamp ({end_ts})')
    log.info(f'Patched {in_pdf} document and wrote {out_pdf} in {duration_secs} secs')

    return 0
