# [[[fill git_describe()]]]
__version__ = '2023.1.21+parent.85ecfd90'
# [[[end]]] (checksum: 9fb8b8c0eb390d5ee5ac54b6fb82cf2b)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)

