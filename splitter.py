import argparse
import pathlib
import os
from PyPDF2 import PdfFileWriter, PdfFileReader
from pathlib import Path


class Config:
    def __init__(self, input, split, output):
        self.input = input
        self.split = split
        self.output = output

        if output is None:
            self.output = Path((os.path.basename(input))).with_suffix('')


def getConfig():
    parser = argparse.ArgumentParser(description="PDF Splitter")

    parser.add_argument("input", help="Input file name", type=pathlib.Path)
    parser.add_argument("split", help="Pages to split", action="extend", nargs="+", type=int)
    parser.add_argument("-o", "--output", help="Output file name")
    parser.add_argument('--version', action='version', version='PDF Splitter 1.0')

    arguments = parser.parse_args()

    return Config(arguments.input, arguments.split, arguments.output)


def split(configuration):
    inputPdf = PdfFileReader(open(configuration.input, "rb"))

    page = 1

    for splitPage in configuration.split:
        splitPdf(inputPdf, configuration.output, page, splitPage)

        page = splitPage + 1


    if page <= inputPdf.numPages:
        splitPdf(inputPdf, configuration.output, page, inputPdf.numPages)

def splitPdf(inputPdf, output, start, end):
    page = start

    print(start, end)

    if start > inputPdf.numPages or end > inputPdf.numPages:
        raise Exception(f"Tried splitting pdf on page {start} until {end} but it only contains {inputPdf.numPages} pages!")

    outputPdf = PdfFileWriter()

    while page <= end:
        outputPdf.addPage(inputPdf.getPage(page - 1))
        page += 1

    with open(f"{configuration.output}({start}-{end}).pdf", "wb") as outputStream:
        outputPdf.write(outputStream)


if __name__ == '__main__':
    configuration = getConfig();

    split(configuration);
