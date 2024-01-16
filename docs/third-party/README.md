# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/etiketti/blob/default/etc/sbom/cdx.json) with SHA256 checksum ([82e4ffc7 ...](https://git.sr.ht/~sthagen/etiketti/blob/default/etc/sbom/cdx.json.sha256 "sha256:82e4ffc7201ac15622ada08cf1675ee042fe5682c9e70f05044d6a82da9f0835")).
<!--[[[end]]] (checksum: a9f00220215954caa1fd2bb4ac2d2203)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                    | Version                                                       | License                              | Author                           | Description (from packaging data)                        |
|:--------------------------------------------------------|:--------------------------------------------------------------|:-------------------------------------|:---------------------------------|:---------------------------------------------------------|
| [PyYAML](https://pyyaml.org/)                           | [6.0](https://pypi.org/project/PyYAML/6.0/)                   | MIT License                          | Kirill Simonov                   | YAML parser and emitter for Python                       |
| [liitos](https://git.sr.ht/~sthagen/liitos)             | [2023.6.17](https://pypi.org/project/liitos/2023.6.17/)       | MIT License                          | Stefan Hagen <stefan@hagen.link> | Splice (Finnish liitos) contributions.                   |
| [navigaattori](https://git.sr.ht/~sthagen/navigaattori) | [2023.6.18](https://pypi.org/project/navigaattori/2023.6.18/) | MIT License                          | Stefan Hagen <stefan@hagen.link> | Navigator (Finnish: navigaattori) guided by conventions. |
| [pikepdf](https://github.com/pikepdf/pikepdf)           | [6.2.8.post1](https://pypi.org/project/pikepdf/6.2.8.post1/)  | Mozilla Public License 2.0 (MPL 2.0) | James R. Barlow                  | Read and write PDFs with Python, powered by qpdf         |
<!--[[[end]]] (checksum: 38d3a42c149f8d4f21a482c9d5834a1b)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                   | Version                                                     | License                                            | Author                                        | Description (from packaging data)                                                                                                         |
|:-------------------------------------------------------|:------------------------------------------------------------|:---------------------------------------------------|:----------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------|
| [click](https://palletsprojects.com/p/click/)          | [8.1.7](https://pypi.org/project/click/8.1.7/)              | BSD License                                        | Pallets <contact@palletsprojects.com>         | Composable command line interface toolkit                                                                                                 |
| [deprecation](http://deprecation.readthedocs.io/)      | [2.1.0](https://pypi.org/project/deprecation/2.1.0/)        | Apache Software License                            | Brian Curtin                                  | A library to handle automated deprecations                                                                                                |
| [foran](https://git.sr.ht/~sthagen/foran)              | [2023.6.19](https://pypi.org/project/foran/2023.6.19/)      | MIT License                                        | Stefan Hagen <stefan@hagen.link>              | In front or behind (Danish: foran eller bagved)? Answering the question if a local repository status is in front of or behind its remote. |
| [gitdb](https://github.com/gitpython-developers/gitdb) | [4.0.11](https://pypi.org/project/gitdb/4.0.11/)            | BSD License                                        | Sebastian Thiel                               | Git Object Database                                                                                                                       |
| [lxml](https://lxml.de/)                               | [5.0.1](https://pypi.org/project/lxml/5.0.1/)               | BSD License                                        | lxml dev team                                 | Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API.                                          |
| [msgspec](https://jcristharif.com/msgspec/)            | [0.18.5](https://pypi.org/project/msgspec/0.18.5/)          | BSD License                                        | Jim Crist-Harif                               | A fast serialization and validation library, with builtin support for JSON, MessagePack, YAML, and TOML.                                  |
| [packaging](https://github.com/pypa/packaging)         | [23.2](https://pypi.org/project/packaging/23.2/)            | Apache Software License; BSD License               | Donald Stufft <donald@stufft.io>              | Core utilities for Python packages                                                                                                        |
| [pillow](https://python-pillow.org)                    | [10.2.0](https://pypi.org/project/pillow/10.2.0/)           | Historical Permission Notice and Disclaimer (HPND) | "Jeffrey A. Clark (Alex)" <aclark@aclark.net> | Python Imaging Library (Fork)                                                                                                             |
| [psutil](https://github.com/giampaolo/psutil)          | [5.9.7](https://pypi.org/project/psutil/5.9.7/)             | BSD License                                        | Giampaolo Rodola                              | Cross-platform lib for process and system monitoring in Python.                                                                           |
| [py-cpuinfo](https://github.com/workhorsy/py-cpuinfo)  | [9.0.0](https://pypi.org/project/py-cpuinfo/9.0.0/)         | MIT License                                        | Matthew Brennan Jones                         | Get CPU info with pure Python                                                                                                             |
| [smmap](https://github.com/gitpython-developers/smmap) | [5.0.1](https://pypi.org/project/smmap/5.0.1/)              | BSD License                                        | Sebastian Thiel                               | A pure Python implementation of a sliding window memory map manager                                                                       |
| [taksonomia](https://git.sr.ht/~sthagen/taksonomia)    | [2023.6.18](https://pypi.org/project/taksonomia/2023.6.18/) | MIT License                                        | Stefan Hagen <stefan@hagen.link>              | Taxonomy (Finnish: taksonomia) of a folder tree, guided by conventions.                                                                   |
| [treelib](https://github.com/caesar0301/treelib)       | [1.7.0](https://pypi.org/project/treelib/1.7.0/)            | Apache Software License                            | Xiaming Chen                                  | A Python implementation of tree structure.                                                                                                |
<!--[[[end]]] (checksum: 802b1591bbb6260c83f9b31481bc5d13)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
liitos==2023.6.17
├── foran [required: >=2022.12.7, installed: 2023.6.19]
│   ├── GitPython [required: >=3.1.31, installed: 3.1.41]
│   │   └── gitdb [required: >=4.0.1,<5, installed: 4.0.11]
│   │       └── smmap [required: >=3.0.1,<6, installed: 5.0.1]
│   └── typer [required: >=0.9.0, installed: 0.9.0]
│       ├── click [required: >=7.1.1,<9.0.0, installed: 8.1.7]
│       └── typing-extensions [required: >=3.7.4.3, installed: 4.9.0]
├── PyYAML [required: >=6.0, installed: 6.0]
├── shellingham [required: >=1.5.0.post1, installed: 1.5.4]
├── taksonomia [required: >=2023.1.24, installed: 2023.6.18]
│   ├── lxml [required: >=4.9.2, installed: 5.0.1]
│   ├── msgspec [required: >=0.16.0, installed: 0.18.5]
│   ├── psutil [required: >=5.9.5, installed: 5.9.7]
│   ├── py-cpuinfo [required: >=9.0.0, installed: 9.0.0]
│   └── PyYAML [required: >=6.0, installed: 6.0]
├── treelib [required: >=1.6.4, installed: 1.7.0]
│   └── six [required: Any, installed: 1.16.0]
└── typer [required: >=0.7.0, installed: 0.9.0]
    ├── click [required: >=7.1.1,<9.0.0, installed: 8.1.7]
    └── typing-extensions [required: >=3.7.4.3, installed: 4.9.0]
navigaattori==2023.6.18
├── foran [required: >=2022.12.7, installed: 2023.6.19]
│   ├── GitPython [required: >=3.1.31, installed: 3.1.41]
│   │   └── gitdb [required: >=4.0.1,<5, installed: 4.0.11]
│   │       └── smmap [required: >=3.0.1,<6, installed: 5.0.1]
│   └── typer [required: >=0.9.0, installed: 0.9.0]
│       ├── click [required: >=7.1.1,<9.0.0, installed: 8.1.7]
│       └── typing-extensions [required: >=3.7.4.3, installed: 4.9.0]
├── PyYAML [required: >=6.0, installed: 6.0]
├── taksonomia [required: >=2022.12.7, installed: 2023.6.18]
│   ├── lxml [required: >=4.9.2, installed: 5.0.1]
│   ├── msgspec [required: >=0.16.0, installed: 0.18.5]
│   ├── psutil [required: >=5.9.5, installed: 5.9.7]
│   ├── py-cpuinfo [required: >=9.0.0, installed: 9.0.0]
│   └── PyYAML [required: >=6.0, installed: 6.0]
├── treelib [required: >=1.6.1, installed: 1.7.0]
│   └── six [required: Any, installed: 1.16.0]
└── typer [required: >=0.7.0, installed: 0.9.0]
    ├── click [required: >=7.1.1,<9.0.0, installed: 8.1.7]
    └── typing-extensions [required: >=3.7.4.3, installed: 4.9.0]
pikepdf==6.2.8.post1
├── deprecation [required: Any, installed: 2.1.0]
│   └── packaging [required: Any, installed: 23.2]
├── lxml [required: >=4.8, installed: 5.0.1]
├── packaging [required: Any, installed: 23.2]
└── pillow [required: >=9.0, installed: 10.2.0]
````
<!--[[[end]]] (checksum: a559f31ed0daaa46f4f250a7ce42f415)-->
