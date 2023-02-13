"""Label (Finnish: etiketti) some files."""
import datetime as dti
import logging
import os
import pathlib
from typing import List, no_type_check

# [[[fill git_describe()]]]
__version__ = '2023.2.13+parent.cd198833'
# [[[end]]] (checksum: a19ffa32f34381baba216ee9e3708c31)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)

APP_NAME = 'Label (Finnish: etiketti) some files.'
APP_ALIAS = 'etiketti'
APP_ENV = 'ETIKETTI'
APP_VERSION = __version__
DEBUG = bool(os.getenv(f'{APP_ENV}_DEBUG', ''))
VERBOSE = bool(os.getenv(f'{APP_ENV}_VERBOSE', ''))
QUIET = False
STRICT = bool(os.getenv(f'{APP_ENV}_STRICT', ''))
ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'
DEFAULT_CONFIG_NAME = '.etiketti.json'
DEFAULT_LF_ONLY = 'YES'
log = logging.getLogger()  # Module level logger is sufficient
LOG_FOLDER = pathlib.Path('logs')
LOG_FILE = f'{APP_ALIAS}.log'
LOG_PATH = pathlib.Path(LOG_FOLDER, LOG_FILE) if LOG_FOLDER.is_dir() else pathlib.Path(LOG_FILE)
LOG_LEVEL = logging.INFO

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
PathLike = str | pathlib.Path

__all__: List[str] = [
    'APP_ALIAS',
    'APP_ENV',
    'APP_NAME',
    'APP_VERSION',
    'CONFIG_PATH_STRING',
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
]


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
