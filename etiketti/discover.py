import hashlib
import io
import pathlib
import platform
import subprocess  # nosec B404
from typing import Any, Callable, no_type_check

import yaml

from etiketti import (
    ENCODING,
    LOG_SEPARATOR,
    ContextType,
    ConventionsType,
    PathLike,
    log,
)

CHUNK_SIZE = 2 << 15


def get_producer() -> str:
    """Assume the producer is fixed and retrieve the terse version repr from a --version call."""
    version_text = 'Version unknown'
    proc = subprocess.Popen(['lualatex', '--version'], stdout=subprocess.PIPE)  # nosec B603, B607
    for line in io.TextIOWrapper(proc.stdout, encoding='utf-8'):  # type: ignore
        if line.startswith('This is LuaHBTeX, Version '):
            version_text = line.rstrip()
            break
    log.info(f'producer version banner: ({version_text})')

    # Example: 'This is LuaHBTeX, Version 1.15.0 (TeX Live 2022)'
    engine = 'lltx'
    version = version_text.split('Version ', 1)[1].rstrip().replace(' (TeX Live ', '-txlv-').rstrip(')')
    where = platform.platform().lower()
    producer_version = f'{engine}-{version}-{where}'
    log.info(f'- noting as: {producer_version=}')
    log.info(LOG_SEPARATOR)
    return producer_version


def hash_file(path: pathlib.Path, hasher: Callable[..., Any] | None = None) -> str:
    """Return the SHA512 hex digest of the data from file."""
    if hasher is None:
        hasher = hashlib.sha512
    the_hash = hasher()
    with open(path, 'rb') as handle:
        while chunk := handle.read(CHUNK_SIZE):
            the_hash.update(chunk)
    return the_hash.hexdigest()


@no_type_check
def load_label_context(path: PathLike) -> ContextType:
    """Load the label context providing prefix, site-id, and action-id."""
    with open(path, 'rt', encoding=ENCODING) as handle:
        return yaml.safe_load(handle)


@no_type_check
def extract_author(path: PathLike) -> str:
    """Extract the author from the approvals file."""
    with open(path, 'rt', encoding=ENCODING) as handle:
        approvals = yaml.safe_load(handle)
    entries = approvals['approvals']
    for entry in entries:
        if entry.get('role').lower() == 'author':
            return entry.get('name', '') or ''
    return ''


def extract_meta_parts(path: PathLike) -> tuple[str, str, str]:
    """Extract the title, subject, keywords in that order from the metadata file."""
    with open(path, 'rt', encoding=ENCODING) as handle:
        metadata = yaml.safe_load(handle)
    mapping = metadata['document']['common']
    title = mapping.get('title', '')
    subject = mapping.get('header_id', '')
    keywords = mapping.get('keywords_csl', '')
    return title or '', subject or '', keywords or ''


def load_conventions(context: ContextType, path: PathLike) -> ConventionsType:
    """Derive conventions from path to input pdf file."""
    in_pdf = pathlib.Path(path)
    workspace = in_pdf.parent
    names = context['label']
    return {
        'workspace-folder-path': workspace,
        'approvals-yml-path': workspace / names.get('approvals-yml-name', 'approvals.yml'),
        'metadata-yml-path': workspace / names.get('metadata-yml-name', 'metadata.yml'),
        'bookmatter-tex-path': workspace / names.get('bookmatter-tex-name', 'bookmatter.tex'),
        'document-tex-path': workspace / names.get('document-tex-name', 'document.tex'),
        'driver-tex-path': workspace / names.get('driver-tex-name', 'driver.tex'),
        'metadata-tex-path': workspace / names.get('metadata-tex-name', 'metadata.tex'),
        'publisher-tex-path': workspace / names.get('publisher-tex-name', 'publisher.tex'),
        'setup-tex-path': workspace / names.get('setup-tex-name', 'setup.tex'),
        'this-tex-path': workspace / names.get('this-tex-name', 'this.tex'),
    }
