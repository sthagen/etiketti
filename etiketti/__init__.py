# [[[fill git_describe()]]]
__version__ = '2023.1.22+parent.1c9b943f'
# [[[end]]] (checksum: 3bd1931402285ec7d6d496ce3b055c6f)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
