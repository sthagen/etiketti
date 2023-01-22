# API

## Example Session:

```python
>>> from etiketti.discover import load_conventions, load_label_context
>>> from etiketti.implementation import cross_correlate, pdf_attributes
2023-01-22T18:06:19.181185+00:00 INFO [pikepdf._qpdf]: pikepdf C++ to Python logger bridge initialized
>>> in_pdf = 'example/deep/render/pdf/this.pdf'
>>> out_pdf = 'labeled.pdf'
>>> cfg_path = 'example/etiketti.yml'
>>> context = load_label_context(cfg_path)
>>> conventions = load_conventions(context, in_pdf)
>>> cross_correlate(source=in_pdf, conventions=conventions, context=context, target=out_pdf)
2023-01-22T18:06:19.251886+00:00 INFO [ETIKETTI]: Retrieving producer information:
2023-01-22T18:06:19.251930+00:00 INFO [ETIKETTI]: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
2023-01-22T18:06:19.255359+00:00 INFO [ETIKETTI]: producer version banner: (This is LuaHBTeX, Version 1.15.0 (TeX Live 2022))
2023-01-22T18:06:19.262069+00:00 INFO [ETIKETTI]: - noting as: producer_version='lltx-1.15.0-txlv-2022-macos-11.7.2-arm64-arm-64bit'
2023-01-22T18:06:19.262153+00:00 INFO [ETIKETTI]: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
2023-01-22T18:06:19.266233+00:00 INFO [ETIKETTI]: - BookmatterTexHash -> sha512:2d46ce8e8df5d1e5402a407a4f1da8123d937eeb013c935304a3a50e38a21959462671022385af11bc2ed845ee9217824a3e1fd6c1bc7d4a0241c609e5cdb10b
2023-01-22T18:06:19.266265+00:00 INFO [ETIKETTI]: - DocumentTexHash   -> sha512:ccc6a03dd69b0a1fa0ab809576ea381abbe5879f8c722ae2a5d8598edb043aab5556ba5ed54915e664b2e6383571353cad609c7b1574bc455074c94cefd2cf40
2023-01-22T18:06:19.266281+00:00 INFO [ETIKETTI]: - DriverTexHash     -> sha512:da21513181c651d3faf40b197049bc0ff743e6a385328d50564babebb34fb31f8416ae44c0eb9226df6a4fb68fcc9d549a2b87978a45103490c8b152c3765910
2023-01-22T18:06:19.266294+00:00 INFO [ETIKETTI]: - MetadataTexHash   -> sha512:742504804e06408e1af021525d4d701cd11eadd8163b03109fed9ca80e31b508599facded70f69d553c355e477bcda662a1c6176355f2a04edd6935960f58ab5
2023-01-22T18:06:19.266307+00:00 INFO [ETIKETTI]: - PublisherTexHash  -> sha512:566d2c7775ed5a83876df9135b70f4cfe618656f79837bc15703f0b0ed7f413b1a3b0a76f88755791b1d70bd410812bf31d421fd5c656451da33ee20b4f2245a
2023-01-22T18:06:19.266319+00:00 INFO [ETIKETTI]: - SetupTexHash      -> sha512:8cbb7f0d2b84194348acb85bd632c4389be21827baeabf8453757b1502054779f8fd34d5b2b202d345d659e1b184c9500ad3b9ea7401a969861b8012e26423ba
2023-01-22T18:06:19.266331+00:00 INFO [ETIKETTI]: - ThisTexHash       -> sha512:da21513181c651d3faf40b197049bc0ff743e6a385328d50564babebb34fb31f8416ae44c0eb9226df6a4fb68fcc9d549a2b87978a45103490c8b152c3765910
2023-01-22T18:06:19.280735+00:00 INFO [ETIKETTI]: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
2023-01-22T18:06:19.280811+00:00 INFO [ETIKETTI]: Patching the timestamps:
2023-01-22T18:06:19.280829+00:00 INFO [ETIKETTI]: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
2023-01-22T18:06:19.280842+00:00 INFO [ETIKETTI]: exiftool "-CreateDate=2023-01-22 17:53:11" "-ModifyDate=2023-01-22 17:53:11" labeled.pdf ...
2023-01-22T18:06:19.436420+00:00 INFO [ETIKETTI]: timestamp-patch:     1 image files updated
2023-01-22T18:06:19.438490+00:00 INFO [ETIKETTI]: ==> Timestamp patch process (exiftool "-CreateDate=2023-01-22 17:53:11" "-ModifyDate=2023-01-22 17:53:11" labeled.pdf) returned 0
2023-01-22T18:06:19.438528+00:00 INFO [ETIKETTI]: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
>>> pdf_attributes(out_pdf)
2023-01-22T18:06:19.439786+00:00 INFO [ETIKETTI]: exiftool labeled.pdf ...
2023-01-22T18:06:19.519213+00:00 INFO [ETIKETTI]: meta-state: ExifTool Version Number         : 12.50
2023-01-22T18:06:19.519401+00:00 INFO [ETIKETTI]: meta-state: File Name                       : labeled.pdf
2023-01-22T18:06:19.519419+00:00 INFO [ETIKETTI]: meta-state: Directory                       : .
2023-01-22T18:06:19.519436+00:00 INFO [ETIKETTI]: meta-state: File Size                       : 46 kB
2023-01-22T18:06:19.519451+00:00 INFO [ETIKETTI]: meta-state: File Modification Date/Time     : 2023:01:22 19:06:19+01:00
2023-01-22T18:06:19.519466+00:00 INFO [ETIKETTI]: meta-state: File Access Date/Time           : 2023:01:22 19:06:19+01:00
2023-01-22T18:06:19.519481+00:00 INFO [ETIKETTI]: meta-state: File Inode Change Date/Time     : 2023:01:22 19:06:19+01:00
2023-01-22T18:06:19.519496+00:00 INFO [ETIKETTI]: meta-state: File Permissions                : -rw-r--r--
2023-01-22T18:06:19.519512+00:00 INFO [ETIKETTI]: meta-state: File Type                       : PDF
2023-01-22T18:06:19.519524+00:00 INFO [ETIKETTI]: meta-state: File Type Extension             : pdf
2023-01-22T18:06:19.519536+00:00 INFO [ETIKETTI]: meta-state: MIME Type                       : application/pdf
2023-01-22T18:06:19.519557+00:00 INFO [ETIKETTI]: meta-state: PDF Version                     : 1.5
2023-01-22T18:06:19.519572+00:00 INFO [ETIKETTI]: meta-state: Linearized                      : No
2023-01-22T18:06:19.519584+00:00 INFO [ETIKETTI]: meta-state: Author                          : An Author
2023-01-22T18:06:19.519596+00:00 INFO [ETIKETTI]: meta-state: Bookmatter Tex Hash             : sha512:2d46ce8e8df5d1e5402a407a4f1da8123d937eeb013c935304a3a50e38a21959462671022385af11bc2ed845ee9217824a3e1fd6c1bc7d4a0241c609e5cdb10b
2023-01-22T18:06:19.519621+00:00 INFO [ETIKETTI]: meta-state: Classification                  : Internal
2023-01-22T18:06:19.519634+00:00 INFO [ETIKETTI]: meta-state: Create Date                     : 2023:01:22 17:53:11
2023-01-22T18:06:19.519645+00:00 INFO [ETIKETTI]: meta-state: Creator                         : liitos 2023.1.21+parent.85ecfd90
2023-01-22T18:06:19.519657+00:00 INFO [ETIKETTI]: meta-state: Document Tex Hash               : sha512:ccc6a03dd69b0a1fa0ab809576ea381abbe5879f8c722ae2a5d8598edb043aab5556ba5ed54915e664b2e6383571353cad609c7b1574bc455074c94cefd2cf40
2023-01-22T18:06:19.519670+00:00 INFO [ETIKETTI]: meta-state: Driver Tex Hash                 : sha512:da21513181c651d3faf40b197049bc0ff743e6a385328d50564babebb34fb31f8416ae44c0eb9226df6a4fb68fcc9d549a2b87978a45103490c8b152c3765910
2023-01-22T18:06:19.519682+00:00 INFO [ETIKETTI]: meta-state: MSIP Label D9272c 50-c 515-4861-9939-24c 65e 703a 54 Action Id: a5682b06-8eb6-4865-809e-a16341072c4e
2023-01-22T18:06:19.519694+00:00 INFO [ETIKETTI]: meta-state: MSIP Label D9272c 50-c 515-4861-9939-24c 65e 703a 54 Content Bits: 0
2023-01-22T18:06:19.519757+00:00 INFO [ETIKETTI]: meta-state: MSIP Label D9272c 50-c 515-4861-9939-24c 65e 703a 54 Enabled: true
2023-01-22T18:06:19.519787+00:00 INFO [ETIKETTI]: meta-state: MSIP Label D9272c 50-c 515-4861-9939-24c 65e 703a 54 Method: Privileged
2023-01-22T18:06:19.519803+00:00 INFO [ETIKETTI]: meta-state: MSIP Label D9272c 50-c 515-4861-9939-24c 65e 703a 54 Name: Internal
2023-01-22T18:06:19.519818+00:00 INFO [ETIKETTI]: meta-state: MSIP Label D9272c 50-c 515-4861-9939-24c 65e 703a 54 Set Date: 2023-01-22T17:53:11Z
2023-01-22T18:06:19.519832+00:00 INFO [ETIKETTI]: meta-state: MSIP Label D9272c 50-c 515-4861-9939-24c 65e 703a 54 Site Id: 199bb307-615a-479c-9793-bae9cca4d8d7
2023-01-22T18:06:19.519845+00:00 INFO [ETIKETTI]: meta-state: Metadata Tex Hash               : sha512:742504804e06408e1af021525d4d701cd11eadd8163b03109fed9ca80e31b508599facded70f69d553c355e477bcda662a1c6176355f2a04edd6935960f58ab5
2023-01-22T18:06:19.519858+00:00 INFO [ETIKETTI]: meta-state: Modify Date                     : 2023:01:22 17:53:11
2023-01-22T18:06:19.519871+00:00 INFO [ETIKETTI]: meta-state: PTEX Full Banner                : cf. pdf.Producer
2023-01-22T18:06:19.519883+00:00 INFO [ETIKETTI]: meta-state: Producer                        : lltx-1.15.0-txlv-2022-macos-11.7.2-arm64-arm-64bit
2023-01-22T18:06:19.519895+00:00 INFO [ETIKETTI]: meta-state: Publisher Tex Hash              : sha512:566d2c7775ed5a83876df9135b70f4cfe618656f79837bc15703f0b0ed7f413b1a3b0a76f88755791b1d70bd410812bf31d421fd5c656451da33ee20b4f2245a
2023-01-22T18:06:19.519907+00:00 INFO [ETIKETTI]: meta-state: Setup Tex Hash                  : sha512:8cbb7f0d2b84194348acb85bd632c4389be21827baeabf8453757b1502054779f8fd34d5b2b202d345d659e1b184c9500ad3b9ea7401a969861b8012e26423ba
2023-01-22T18:06:19.520433+00:00 INFO [ETIKETTI]: meta-state: Subject                         : P99999
2023-01-22T18:06:19.520453+00:00 INFO [ETIKETTI]: meta-state: This Tex Hash                   : sha512:da21513181c651d3faf40b197049bc0ff743e6a385328d50564babebb34fb31f8416ae44c0eb9226df6a4fb68fcc9d549a2b87978a45103490c8b152c3765910
2023-01-22T18:06:19.520467+00:00 INFO [ETIKETTI]: meta-state: Title                           : Ttt Tt Tt
2023-01-22T18:06:19.520479+00:00 INFO [ETIKETTI]: meta-state: Trapped                         : False
2023-01-22T18:06:19.520492+00:00 INFO [ETIKETTI]: meta-state: Unique Identity                 : a4d86ff8-7d3e-4719-9f45-4bb65f471453
2023-01-22T18:06:19.520504+00:00 INFO [ETIKETTI]: meta-state: Page Mode                       : UseOutlines
2023-01-22T18:06:19.520516+00:00 INFO [ETIKETTI]: meta-state: Page Count                      : 10
2023-01-22T18:06:19.520528+00:00 INFO [ETIKETTI]: meta-state: XMP Toolkit                     : Image::ExifTool 12.50
2023-01-22T18:06:19.520570+00:00 INFO [ETIKETTI]: ==> Meta-state process (exiftool labeled.pdf) returned 0
2023-01-22T18:06:19.520586+00:00 INFO [ETIKETTI]: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
>>>
```

## Help

The usual `help` function works as all functions provide docstrings:

```python
>>> import etiketti.implementation
>>> help(etiketti.implementation)
Help on module etiketti.implementation in etiketti:

NAME
    etiketti.implementation - Implementation API for labeling.

FUNCTIONS
    camelize_first_two(dashed_key: str) -> str
        Transform kebab-key-input into KebabKey.

    cross_correlate(source: str | pathlib.Path, conventions: dict[str, pathlib.Path], context: dict[str, dict[str, str]], target: str | pathlib.Path) -> None
        Load information per conventions and mix with source to create target pdf.

    log_subprocess_output(pipe, prefix: str)

    patch(options: argparse.Namespace) -> int
        Patch the two related meta structures of the pdf file

    pdf_attributes(path: str | pathlib.Path) -> None
        Let exiftool assess the attributes.

    pdf_info(path: str | pathlib.Path) -> None
        Let pdfinfo assess some attributes.

    timestamp_patch(create_date: str, modify_date: str, path: str | pathlib.Path) -> None
        Let exiftool patch the time fields.

DATA
    CREATOR_NAME = 'liitos'
    CREATOR_VERSION = '2023.1.21+parent.85ecfd90'
    ContextType = dict[str, dict[str, str]]
    ConventionsType = dict[str, pathlib.Path]
    ENCODING = 'utf-8'
    LOG_SEPARATOR = '- - - - - - - - - - - - - - - - - - - - - - - - ... -...
    PathLike = str | pathlib.Path
    TS_FORMAT_ISO = '%Y-%m-%dT%H:%M:%SZ'
    TS_FORMAT_PATCH = '%Y-%m-%d %H:%M:%S'
    TS_FORMAT_PAYLOADS = '%Y-%m-%d %H:%M:%S.%f UTC'
    log = <Logger ETIKETTI (INFO)>

FILE
    /Users/ruth/d/gh/sha/src/etiketti/etiketti/implementation.py

```
