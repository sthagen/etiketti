"""Command line interface for labeling."""
import argparse
import pathlib
import sys

import etiketti.implementation as impl
from etiketti import (
    APP_ALIAS,
    APP_NAME,
    APP_VERSION,
    CONFIG_PATH_STRING,
    SOURCE_NAME_PATH_STRING,
    TARGET_NAME_PATH_STRING,
)


def parse_request(argv: list[str]) -> int | argparse.Namespace:
    """DRY."""
    parser = argparse.ArgumentParser(
        prog=APP_ALIAS, description=APP_NAME, formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '--in-path',
        '-i',
        dest='in_pdf',
        default='',
        help='input file path to pdf file to label',
        required=False,
    )
    parser.add_argument(
        'in_pdf_pos',
        nargs='?',
        default=SOURCE_NAME_PATH_STRING,
        help='input file path to pdf file to label',
    )
    parser.add_argument(
        '--out-path',
        '-o',
        dest='out_pdf',
        default=TARGET_NAME_PATH_STRING,
        help='output path for resulting labeled pdf file',
        required=False,
    )
    parser.add_argument(
        '--config',
        '-c',
        dest='cfg_path',
        default=CONFIG_PATH_STRING,
        help='configuration file for label context data',
        required=False,
    )
    parser.add_argument(
        '--enforce',
        '-e',
        dest='enforce',
        default=False,
        action='store_true',
        help='enforce labels by overwriting the source file',
        required=False,
    )
    parser.add_argument(
        '--version',
        '-V',
        dest='version_request',
        default=False,
        action='store_true',
        help='show version of the app and exit',
        required=False,
    )

    if not argv:
        print(f'{APP_NAME} version {APP_VERSION}')
        parser.print_help()
        return 0

    options = parser.parse_args(argv)

    if options.version_request:
        print(f'{APP_NAME} version {APP_VERSION}')
        return 0

    if not options.in_pdf:
        if options.in_pdf_pos:
            options.in_pdf = options.in_pdf_pos
        else:
            options.in_pdf = SOURCE_NAME_PATH_STRING

    in_pdf = pathlib.Path(options.in_pdf)
    if in_pdf.exists():
        if in_pdf.is_file():
            cfg_path = pathlib.Path(options.cfg_path)
            if cfg_path.exists():
                if cfg_path.is_file():
                    return options
                parser.error(f'configuration path ({cfg_path}) is not a file')
            parser.error(f'configuration path ({cfg_path}) does not exist')
        parser.error(f'requested pdf at ({in_pdf}) is not a file')
    parser.error(f'requested pdf at ({in_pdf}) does not exist')


def app(argv: list[str] | None = None) -> int:
    """Delegate processing to functional module."""
    argv = sys.argv[1:] if argv is None else argv
    options = parse_request(argv)
    if isinstance(options, int):
        return 0
    return impl.patch(options)
