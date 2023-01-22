# Usage

Simple specialized labeling application - probably not useful to many.

## Help

Calling the app with no arguments yields a help display:

```console
❯ etiketti
2023-01-22T17:41:25.526925+00:00 INFO [pikepdf._qpdf]: pikepdf C++ to Python logger bridge initialized
usage: etiketti [-h] [--in-path IN_PDF] [--out-path OUT_PDF] [--config CFG_PATH] [--enforce] [in_pdf_pos]

Label (Finnish: etiketti) some files.

positional arguments:
  in_pdf_pos            input file path to pdf file to label

options:
  -h, --help            show this help message and exit
  --in-path IN_PDF, -i IN_PDF
                        input file path to pdf file to label
  --out-path OUT_PDF, -o OUT_PDF
                        output path for resulting labeled pdf file
  --config CFG_PATH, -c CFG_PATH
                        configuration file for label context data
  --enforce, -e         enforce labels by overwriting the source file
```

## Example:

Using the rendering result below an 
[example folder of `liitos`](https://git.sr.ht/~sthagen/liitos/tree/default/item/example/deep) to
label the resulting `this.pdf`:

```console
❯ etiketti example/deep/render/pdf/this.pdf -c example/etiketti.yml 2>&1 | cut -c34- | sed "s/NAVIGAATTORI/.../g; s/WARNING/W/g; s/ERROR/E/g; s/INFO/I/g;"
I [pikepdf._qpdf]: pikepdf C++ to Python logger bridge initialized
I [ETIKETTI]: Patching pdf meta data of example/deep/render/pdf/this.pdf
I [ETIKETTI]: Configuration path is example/etiketti.yml
I [ETIKETTI]: Output path is labeled.pdf
I [ETIKETTI]: Labeling will NOT be enforced - example/deep/render/pdf/this.pdf will not be modified
I [ETIKETTI]: Start timestamp (2023-01-22 17:54:53.766851 UTC)
I [ETIKETTI]: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
I [ETIKETTI]: loaded label context:
I [ETIKETTI]: - prefix            -> MSIP_Label_d9272c50-c515-4861-9939-24c65e703a54_
I [ETIKETTI]: - site-id           -> 199bb307-615a-479c-9793-bae9cca4d8d7
I [ETIKETTI]: - action-id         -> a5682b06-8eb6-4865-809e-a16341072c4e
I [ETIKETTI]: - approvals-yml-name -> approvals.yml
I [ETIKETTI]: - metadata-yml-name -> metadata.yml
I [ETIKETTI]: - bookmatter-tex-name -> bookmatter.tex
I [ETIKETTI]: - document-tex-name -> document.tex
I [ETIKETTI]: - driver-tex-name   -> driver.tex
I [ETIKETTI]: - metadata-tex-name -> metadata.tex
I [ETIKETTI]: - publisher-tex-name -> publisher.tex
I [ETIKETTI]: - setup-tex-name    -> setup.tex
I [ETIKETTI]: - this-tex-name     -> this.tex
I [ETIKETTI]: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
I [ETIKETTI]: identified conventions:
I [ETIKETTI]: - workspace-folder-path -> example/deep/render/pdf
I [ETIKETTI]: - approvals-yml-path -> example/deep/render/pdf/approvals.yml
I [ETIKETTI]: - metadata-yml-path -> example/deep/render/pdf/metadata.yml
I [ETIKETTI]: - bookmatter-tex-path -> example/deep/render/pdf/bookmatter.tex
I [ETIKETTI]: - document-tex-path -> example/deep/render/pdf/document.tex
I [ETIKETTI]: - driver-tex-path   -> example/deep/render/pdf/driver.tex
I [ETIKETTI]: - metadata-tex-path -> example/deep/render/pdf/metadata.tex
I [ETIKETTI]: - publisher-tex-path -> example/deep/render/pdf/publisher.tex
I [ETIKETTI]: - setup-tex-path    -> example/deep/render/pdf/setup.tex
I [ETIKETTI]: - this-tex-path     -> example/deep/render/pdf/this.tex
I [ETIKETTI]: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
I [ETIKETTI]: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
I [ETIKETTI]: PDF information from source file:
I [ETIKETTI]: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
I [ETIKETTI]: pdfinfo example/deep/render/pdf/this.pdf ...
I [ETIKETTI]: pdf-info: Title:
I [ETIKETTI]: pdf-info: Subject:
I [ETIKETTI]: pdf-info: Keywords:
I [ETIKETTI]: pdf-info: Author:
I [ETIKETTI]: pdf-info: Creator:         LaTeX with hyperref
I [ETIKETTI]: pdf-info: Producer:        LuaTeX-1.15.0
I [ETIKETTI]: pdf-info: CreationDate:    Sun Jan 22 18:53:09 2023 CET
I [ETIKETTI]: pdf-info: ModDate:         Sun Jan 22 18:53:09 2023 CET
I [ETIKETTI]: pdf-info: Custom Metadata: yes
I [ETIKETTI]: pdf-info: Metadata Stream: no
I [ETIKETTI]: pdf-info: Tagged:          no
I [ETIKETTI]: pdf-info: UserProperties:  no
I [ETIKETTI]: pdf-info: Suspects:        no
I [ETIKETTI]: pdf-info: Form:            none
I [ETIKETTI]: pdf-info: JavaScript:      no
I [ETIKETTI]: pdf-info: Pages:           10
I [ETIKETTI]: pdf-info: Encrypted:       no
I [ETIKETTI]: pdf-info: Page size:       595.276 x 841.89 pts (A4)
I [ETIKETTI]: pdf-info: Page rot:        0
I [ETIKETTI]: pdf-info: File size:       39072 bytes
I [ETIKETTI]: pdf-info: Optimized:       no
I [ETIKETTI]: pdf-info: PDF version:     1.5
I [ETIKETTI]: ==> Pdfinfo process (pdfinfo example/deep/render/pdf/this.pdf) returned 0
I [ETIKETTI]: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
I [ETIKETTI]: PDF attributes/labels from source file:
I [ETIKETTI]: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
I [ETIKETTI]: exiftool example/deep/render/pdf/this.pdf ...
I [ETIKETTI]: meta-state: ExifTool Version Number         : 12.50
I [ETIKETTI]: meta-state: File Name                       : this.pdf
I [ETIKETTI]: meta-state: Directory                       : example/deep/render/pdf
I [ETIKETTI]: meta-state: File Size                       : 39 kB
I [ETIKETTI]: meta-state: File Modification Date/Time     : 2023:01:22 18:53:11+01:00
I [ETIKETTI]: meta-state: File Access Date/Time           : 2023:01:22 18:53:11+01:00
I [ETIKETTI]: meta-state: File Inode Change Date/Time     : 2023:01:22 18:53:11+01:00
I [ETIKETTI]: meta-state: File Permissions                : -rw-r--r--
I [ETIKETTI]: meta-state: File Type                       : PDF
I [ETIKETTI]: meta-state: File Type Extension             : pdf
I [ETIKETTI]: meta-state: MIME Type                       : application/pdf
I [ETIKETTI]: meta-state: PDF Version                     : 1.5
I [ETIKETTI]: meta-state: Linearized                      : No
I [ETIKETTI]: meta-state: Page Count                      : 10
I [ETIKETTI]: meta-state: Page Mode                       : UseOutlines
I [ETIKETTI]: meta-state: Author                          :
I [ETIKETTI]: meta-state: Title                           :
I [ETIKETTI]: meta-state: Subject                         :
I [ETIKETTI]: meta-state: Creator                         : LaTeX with hyperref
I [ETIKETTI]: meta-state: Producer                        : LuaTeX-1.15.0
I [ETIKETTI]: meta-state: Create Date                     : 2023:01:22 18:53:09+01:00
I [ETIKETTI]: meta-state: Modify Date                     : 2023:01:22 18:53:09+01:00
I [ETIKETTI]: meta-state: Trapped                         : False
I [ETIKETTI]: meta-state: PTEX Full Banner                : This is LuaHBTeX, Version 1.15.0 (TeX Live 2022)
I [ETIKETTI]: ==> Meta-state process (exiftool example/deep/render/pdf/this.pdf) returned 0
I [ETIKETTI]: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
I [ETIKETTI]: Retrieving producer information:
I [ETIKETTI]: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
I [ETIKETTI]: producer version banner: (This is LuaHBTeX, Version 1.15.0 (TeX Live 2022))
I [ETIKETTI]: - noting as: producer_version='lltx-1.15.0-txlv-2022-macos-11.7.2-arm64-arm-64bit'
I [ETIKETTI]: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
I [ETIKETTI]: - BookmatterTexHash -> sha512:2d46ce8e8df5d1e5402a407a4f1da8123d937eeb013c935304a3a50e38a21959462671022385af11bc2ed845ee9217824a3e1fd6c1bc7d4a0241c609e5cdb10b
I [ETIKETTI]: - DocumentTexHash   -> sha512:ccc6a03dd69b0a1fa0ab809576ea381abbe5879f8c722ae2a5d8598edb043aab5556ba5ed54915e664b2e6383571353cad609c7b1574bc455074c94cefd2cf40
I [ETIKETTI]: - DriverTexHash     -> sha512:da21513181c651d3faf40b197049bc0ff743e6a385328d50564babebb34fb31f8416ae44c0eb9226df6a4fb68fcc9d549a2b87978a45103490c8b152c3765910
I [ETIKETTI]: - MetadataTexHash   -> sha512:742504804e06408e1af021525d4d701cd11eadd8163b03109fed9ca80e31b508599facded70f69d553c355e477bcda662a1c6176355f2a04edd6935960f58ab5
I [ETIKETTI]: - PublisherTexHash  -> sha512:566d2c7775ed5a83876df9135b70f4cfe618656f79837bc15703f0b0ed7f413b1a3b0a76f88755791b1d70bd410812bf31d421fd5c656451da33ee20b4f2245a
I [ETIKETTI]: - SetupTexHash      -> sha512:8cbb7f0d2b84194348acb85bd632c4389be21827baeabf8453757b1502054779f8fd34d5b2b202d345d659e1b184c9500ad3b9ea7401a969861b8012e26423ba
I [ETIKETTI]: - ThisTexHash       -> sha512:da21513181c651d3faf40b197049bc0ff743e6a385328d50564babebb34fb31f8416ae44c0eb9226df6a4fb68fcc9d549a2b87978a45103490c8b152c3765910
I [ETIKETTI]: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
I [ETIKETTI]: Patching the timestamps:
I [ETIKETTI]: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
I [ETIKETTI]: exiftool "-CreateDate=2023-01-22 17:53:11" "-ModifyDate=2023-01-22 17:53:11" labeled.pdf ...
I [ETIKETTI]: timestamp-patch:     1 image files updated
I [ETIKETTI]: ==> Timestamp patch process (exiftool "-CreateDate=2023-01-22 17:53:11" "-ModifyDate=2023-01-22 17:53:11" labeled.pdf) returned 0
I [ETIKETTI]: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
I [ETIKETTI]: PDF attributes/labels from target file:
I [ETIKETTI]: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
I [ETIKETTI]: exiftool labeled.pdf ...
I [ETIKETTI]: meta-state: ExifTool Version Number         : 12.50
I [ETIKETTI]: meta-state: File Name                       : labeled.pdf
I [ETIKETTI]: meta-state: Directory                       : .
I [ETIKETTI]: meta-state: File Size                       : 46 kB
I [ETIKETTI]: meta-state: File Modification Date/Time     : 2023:01:22 18:54:54+01:00
I [ETIKETTI]: meta-state: File Access Date/Time           : 2023:01:22 18:54:54+01:00
I [ETIKETTI]: meta-state: File Inode Change Date/Time     : 2023:01:22 18:54:54+01:00
I [ETIKETTI]: meta-state: File Permissions                : -rw-r--r--
I [ETIKETTI]: meta-state: File Type                       : PDF
I [ETIKETTI]: meta-state: File Type Extension             : pdf
I [ETIKETTI]: meta-state: MIME Type                       : application/pdf
I [ETIKETTI]: meta-state: PDF Version                     : 1.5
I [ETIKETTI]: meta-state: Linearized                      : No
I [ETIKETTI]: meta-state: Author                          : An Author
I [ETIKETTI]: meta-state: Bookmatter Tex Hash             : sha512:2d46ce8e8df5d1e5402a407a4f1da8123d937eeb013c935304a3a50e38a21959462671022385af11bc2ed845ee9217824a3e1fd6c1bc7d4a0241c609e5cdb10b
I [ETIKETTI]: meta-state: Classification                  : Internal
I [ETIKETTI]: meta-state: Create Date                     : 2023:01:22 17:53:11
I [ETIKETTI]: meta-state: Creator                         : liitos 2023.1.21+parent.85ecfd90
I [ETIKETTI]: meta-state: Document Tex Hash               : sha512:ccc6a03dd69b0a1fa0ab809576ea381abbe5879f8c722ae2a5d8598edb043aab5556ba5ed54915e664b2e6383571353cad609c7b1574bc455074c94cefd2cf40
I [ETIKETTI]: meta-state: Driver Tex Hash                 : sha512:da21513181c651d3faf40b197049bc0ff743e6a385328d50564babebb34fb31f8416ae44c0eb9226df6a4fb68fcc9d549a2b87978a45103490c8b152c3765910
I [ETIKETTI]: meta-state: MSIP Label D9272c 50-c 515-4861-9939-24c 65e 703a 54 Action Id: a5682b06-8eb6-4865-809e-a16341072c4e
I [ETIKETTI]: meta-state: MSIP Label D9272c 50-c 515-4861-9939-24c 65e 703a 54 Content Bits: 0
I [ETIKETTI]: meta-state: MSIP Label D9272c 50-c 515-4861-9939-24c 65e 703a 54 Enabled: true
I [ETIKETTI]: meta-state: MSIP Label D9272c 50-c 515-4861-9939-24c 65e 703a 54 Method: Privileged
I [ETIKETTI]: meta-state: MSIP Label D9272c 50-c 515-4861-9939-24c 65e 703a 54 Name: Internal
I [ETIKETTI]: meta-state: MSIP Label D9272c 50-c 515-4861-9939-24c 65e 703a 54 Set Date: 2023-01-22T17:53:11Z
I [ETIKETTI]: meta-state: MSIP Label D9272c 50-c 515-4861-9939-24c 65e 703a 54 Site Id: 199bb307-615a-479c-9793-bae9cca4d8d7
I [ETIKETTI]: meta-state: Metadata Tex Hash               : sha512:742504804e06408e1af021525d4d701cd11eadd8163b03109fed9ca80e31b508599facded70f69d553c355e477bcda662a1c6176355f2a04edd6935960f58ab5
I [ETIKETTI]: meta-state: Modify Date                     : 2023:01:22 17:53:11
I [ETIKETTI]: meta-state: PTEX Full Banner                : cf. pdf.Producer
I [ETIKETTI]: meta-state: Producer                        : lltx-1.15.0-txlv-2022-macos-11.7.2-arm64-arm-64bit
I [ETIKETTI]: meta-state: Publisher Tex Hash              : sha512:566d2c7775ed5a83876df9135b70f4cfe618656f79837bc15703f0b0ed7f413b1a3b0a76f88755791b1d70bd410812bf31d421fd5c656451da33ee20b4f2245a
I [ETIKETTI]: meta-state: Setup Tex Hash                  : sha512:8cbb7f0d2b84194348acb85bd632c4389be21827baeabf8453757b1502054779f8fd34d5b2b202d345d659e1b184c9500ad3b9ea7401a969861b8012e26423ba
I [ETIKETTI]: meta-state: Subject                         : P99999
I [ETIKETTI]: meta-state: This Tex Hash                   : sha512:da21513181c651d3faf40b197049bc0ff743e6a385328d50564babebb34fb31f8416ae44c0eb9226df6a4fb68fcc9d549a2b87978a45103490c8b152c3765910
I [ETIKETTI]: meta-state: Title                           : Ttt Tt Tt
I [ETIKETTI]: meta-state: Trapped                         : False
I [ETIKETTI]: meta-state: Unique Identity                 : aec1d9b0-8d10-409d-845f-edae4314ce85
I [ETIKETTI]: meta-state: Page Mode                       : UseOutlines
I [ETIKETTI]: meta-state: Page Count                      : 10
I [ETIKETTI]: meta-state: XMP Toolkit                     : Image::ExifTool 12.50
I [ETIKETTI]: ==> Meta-state process (exiftool labeled.pdf) returned 0
I [ETIKETTI]: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
I [ETIKETTI]: PDF information from target file:
I [ETIKETTI]: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
I [ETIKETTI]: pdfinfo labeled.pdf ...
I [ETIKETTI]: pdf-info: Title:           Ttt Tt Tt
I [ETIKETTI]: pdf-info: Subject:         P99999
I [ETIKETTI]: pdf-info: Keywords:
I [ETIKETTI]: pdf-info: Author:          An Author
I [ETIKETTI]: pdf-info: Creator:         liitos 2023.1.21+parent.85ecfd90
I [ETIKETTI]: pdf-info: Producer:        lltx-1.15.0-txlv-2022-macos-11.7.2-arm64-arm-64bit
I [ETIKETTI]: pdf-info: CreationDate:    Sun Jan 22 18:53:11 2023 CET
I [ETIKETTI]: pdf-info: ModDate:         Sun Jan 22 18:53:11 2023 CET
I [ETIKETTI]: pdf-info: Custom Metadata: yes
I [ETIKETTI]: pdf-info: Metadata Stream: yes
I [ETIKETTI]: pdf-info: Tagged:          no
I [ETIKETTI]: pdf-info: UserProperties:  no
I [ETIKETTI]: pdf-info: Suspects:        no
I [ETIKETTI]: pdf-info: Form:            none
I [ETIKETTI]: pdf-info: JavaScript:      no
I [ETIKETTI]: pdf-info: Pages:           10
I [ETIKETTI]: pdf-info: Encrypted:       no
I [ETIKETTI]: pdf-info: Page size:       595.276 x 841.89 pts (A4)
I [ETIKETTI]: pdf-info: Page rot:        0
I [ETIKETTI]: pdf-info: File size:       45679 bytes
I [ETIKETTI]: pdf-info: Optimized:       no
I [ETIKETTI]: pdf-info: PDF version:     1.5
I [ETIKETTI]: ==> Pdfinfo process (pdfinfo labeled.pdf) returned 0
I [ETIKETTI]: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
I [ETIKETTI]: End timestamp (2023-01-22 17:54:54.142085 UTC)
I [ETIKETTI]: Patched example/deep/render/pdf/this.pdf document and wrote labeled.pdf in 0.375234 secs
```

The context file (configuration) from `example/etiketti.yml` has the following content:

```yaml
---
label:
  prefix: MSIP_Label_d9272c50-c515-4861-9939-24c65e703a54_
  site-id: 199bb307-615a-479c-9793-bae9cca4d8d7
  action-id: a5682b06-8eb6-4865-809e-a16341072c4e
  approvals-yml-name: approvals.yml
  metadata-yml-name: metadata.yml
  bookmatter-tex-name: bookmatter.tex
  document-tex-name: document.tex
  driver-tex-name: driver.tex
  metadata-tex-name: metadata.tex
  publisher-tex-name: publisher.tex
  setup-tex-name: setup.tex
  this-tex-name: this.tex
```
