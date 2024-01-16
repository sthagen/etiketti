"""Label (Finnish: etiketti) some files."""
import datetime as dti
import logging
import os
import pathlib
from typing import Union, no_type_check

# [[[fill git_describe()]]]
__version__ = '2024.1.16+parent.g0a2f67d3'
# [[[end]]] (checksum: e04ad0c0084645e3a7b0cdf9c3f06a99)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)

APP_ALIAS = str(pathlib.Path(__file__).parent.name)
APP_ENV = APP_ALIAS.upper()
APP_NAME = locals()['__doc__']
DEBUG = bool(os.getenv(f'{APP_ENV}_DEBUG', ''))
VERBOSE = bool(os.getenv(f'{APP_ENV}_VERBOSE', ''))
QUIET = False
STRICT = bool(os.getenv(f'{APP_ENV}_STRICT', ''))
ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'
DEFAULT_CONFIG_NAME = f'.{APP_ALIAS}.json'

APP_VERSION = __version__
DEFAULT_LF_ONLY = 'YES'
DEFAULT_AUTHOR = os.getenv(f'{APP_ENV}_DEFAULT_AUTHOR', '')
log = logging.getLogger()  # Module level logger is sufficient
LOG_FOLDER = pathlib.Path('logs')
LOG_FILE = f'{APP_ALIAS}.log'
LOG_PATH = pathlib.Path(LOG_FOLDER, LOG_FILE) if LOG_FOLDER.is_dir() else pathlib.Path(LOG_FILE)
LOG_LEVEL = logging.INFO

COMMA = ','
EQUAL = '='

LOG_SEPARATOR = '- ' * 80
INTER_PROCESS_SYNC_SECS = 0.1
INTER_PROCESS_SYNC_ATTEMPTS = 10
TS_FORMAT_ISO = '%Y-%m-%dT%H:%M:%SZ'
TS_FORMAT_PDF = '%Y%m%dT%H%M%SZ'  # was 'D:%Y%m%dT%H%M%SZ'
TS_FORMAT_LOG = '%Y-%m-%dT%H:%M:%S'
TS_FORMAT_PAYLOADS = '%Y-%m-%d %H:%M:%S.%f UTC'
TS_FORMAT_PATCH = '%Y-%m-%d %H:%M:%S'

SOURCE_NAME_PATH_STRING = os.getenv(f'{APP_ENV}_SOURCE_NAME_PATH_STRING', 'this.pdf')
TARGET_NAME_PATH_STRING = os.getenv(f'{APP_ENV}_TARGET_NAME_PATH_STRING', 'labeled.pdf')
CONFIG_PATH_STRING = os.getenv(f'{APP_ENV}_CONFIG_PATH_STRING', f'/opt/label/{APP_ALIAS}.yml')

ContextType = dict[str, dict[str, str]]
ConventionsType = dict[str, pathlib.Path]
PathLike = Union[str, pathlib.Path]

__all__: list[str] = [
    'APP_ALIAS',
    'APP_ENV',
    'APP_NAME',
    'APP_VERSION',
    'CONFIG_PATH_STRING',
    'DEFAULT_AUTHOR',
    'ENCODING',
    'LOG_SEPARATOR',
    'SOURCE_NAME_PATH_STRING',
    'TARGET_NAME_PATH_STRING',
    'TS_FORMAT_PATCH',
    'TS_FORMAT_PAYLOADS',
    'TS_FORMAT_ISO',
    'ContextType',
    'ConventionsType',
    'PathLike',
    'log',
    'parse_key_value_pair_csl',
]


def parse_key_value_pair_csl(csl: str) -> dict[str, str]:
    """DRY."""
    pairs = [pair.strip() for pair in csl.split(COMMA) if pair.strip() and EQUAL in pair]
    key_value_store = {}
    for pair in pairs:
        try:
            k, v = pair.split(EQUAL, 1)
        except ValueError:
            continue
        real_key = k.strip()
        if real_key:
            key_value_store[real_key] = v.strip()
    return key_value_store


@no_type_check
def formatTime_RFC3339(self, record, datefmt=None):  # noqa
    """HACK A DID ACK we could inject .astimezone() to localize ..."""
    return dti.datetime.fromtimestamp(record.created, dti.timezone.utc).isoformat()  # pragma: no cover


@no_type_check
def init_logger(name=None, level=None):
    """Initialize module level logger"""
    global log  # pylint: disable=global-statement

    log_format = {
        'format': '%(asctime)s %(levelname)s [%(name)s]: %(message)s',
        'datefmt': TS_FORMAT_LOG,
        # 'filename': LOG_PATH,
        'level': LOG_LEVEL if level is None else level,
    }
    logging.Formatter.formatTime = formatTime_RFC3339
    logging.basicConfig(**log_format)
    log = logging.getLogger(APP_ENV if name is None else name)
    log.propagate = True


init_logger(name=APP_ENV, level=logging.DEBUG if DEBUG else None)
