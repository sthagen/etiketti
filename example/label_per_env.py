#! /usr/bin/env python
import datetime as dti
import os
import pathlib
import platform
import subprocess
import uuid

from pikepdf import Pdf

TS_FORMAT_ISO = '%Y-%m-%dT%H:%M:%SZ'
TS_FORMAT_PDF = '%Y%m%dT%H%M%SZ'  # was 'D:%Y%m%dT%H%M%SZ'
TS_FORMAT_LOG = '%Y-%m-%dT%H:%M:%S'
TS_FORMAT_PAYLOADS = '%Y-%m-%d %H:%M:%S.%f UTC'
TS_FORMAT_PATCH = '%Y-%m-%d %H:%M:%S'

EMPTY_HASH = (
    'sha512:'
    'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce'
    '47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e'
)
AUTHOR = os.getenv('ETIKETTI_AUTHOR', '')
TITLE = os.getenv('ETIKETTI_TITLE', '')
SUBJECT = os.getenv('ETIKETTI_SUBJECT', '')
KEYWORDS = os.getenv('ETIKETTI_KEYWORDS', '')
SOURCE_HASH = os.getenv('ETIKETTI_SOURCE_HASH', EMPTY_HASH)
SOURCE_PDF = os.getenv('ETIKETTI_SOURCE_PDF', 'this.pdf')
TARGET_PDF = os.getenv('ETIKETTI_TARGET_PDF', 'labeled.pdf')
PathLike = str | pathlib.Path

source = pathlib.Path(SOURCE_PDF)
target = pathlib.Path(TARGET_PDF)
backend_version = 'cf. pdf.Producer'  # backend_version  # 'putki 2023.1.1'

producer_version = f'lltx-1.15.0-txlv-2022-{platform.platform().lower()}'
creator_version = f'liitos 2023.1.21+parent.85ecfd90'

author = AUTHOR
title = TITLE
subject = SUBJECT
keywords = KEYWORDS
dc_subject = subject
dc_creator = [author]
dc_title = title
keywords = keywords
hashes = {'SourceHash': SOURCE_HASH}
st = source.stat()
c_time_patch = dti.datetime.fromtimestamp(st.st_ctime, tz=dti.timezone.utc).strftime(TS_FORMAT_PATCH)

m_time_iso = dti.datetime.fromtimestamp(st.st_mtime, tz=dti.timezone.utc).strftime(TS_FORMAT_ISO)
m_time_patch = dti.datetime.fromtimestamp(st.st_mtime, tz=dti.timezone.utc).strftime(TS_FORMAT_PATCH)

make_unique = str(uuid.uuid4())

def timestamp_patch(create_date: str, modify_date: str, path: PathLike) -> None:
    """Let exiftool patch the time fields."""
    # on linux the below twisted c->m and m->c mappings gives the correct timestamps
    exiftool_command = f'exiftool "-CreateDate={create_date}" "-ModifyDate={modify_date}" {path}'
    process = subprocess.Popen(
        exiftool_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True  # nosec B602
    )
    return_code = process.wait()


with Pdf.open(source) as pdf:
    with pdf.open_metadata(set_pikepdf_as_editor=False) as m:
        m.load_from_docinfo(pdf.docinfo)
        m['UniqueIdentity'] = make_unique
        m['xmp:CreateDate'] = c_time_patch
        m['xmp:ModifyDate'] = m_time_patch
        m['xmp:CreatorTool'] = creator_version
        m['pdf:Producer'] = producer_version
        m['dc:subject'] = dc_subject
        m['dc:title'] = dc_title
        m['dc:creator'] = dc_creator
        for k, v in hashes.items():
            m[k] = v
        pdf.docinfo['/UniqueIdentity'] = m['UniqueIdentity']
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

timestamp_patch(create_date=m_time_patch, modify_date=c_time_patch, path=target)

