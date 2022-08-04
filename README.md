# PDF Splitter

PDF splitter easily allows you to split pds into smaller pdfs.

## Install

You'll need a minimal Python 3.6 installation and need to install `PyPDF2`:

```bash
pip install PyPDF2
```

## Usage

You can split an input file on the tenth page as such:

```bash
python splitter.py inputfile.pdf 10
```

This will create 2 pdf's: one from the first page until the tenth and one from the eleventh page until the last page of the pdf.

It is possible to add multiple splitting points:

```bash
python splitter.py inputfile.pdf 10 20 25
```

This will create 4 pdfs.

By default the input name will be chosen to create the splitted pdf files, you can change this by providing an output name:

```bash
python splitter.py -o hi inputfile.pdf 10
```

## Credits

- [rubenvanassche](https://github.com/rubenvanassche)
- [All Contributors](../../contributors)

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.
