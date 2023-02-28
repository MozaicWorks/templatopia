import argparse
import sys
from pathlib import Path

from ConsoleWriter import ConsoleWriter
from FileWriter import FileWriter
from TableReaderFromCsv import CsvReader
from TemplatedRow import RowTemplate
from transformer import Template


def main():
    parser = argparse.ArgumentParser(
                    prog = 'templatopia',
                    description = 'Creates files from a template file and a table, using Mustache for templating.',
    )
    parser.add_argument("--template", required=True,
            help="The name of the template file. Eg. template.svg, template.eml")
    parser.add_argument("--from-csv", required=False,
            help="The csv file containing the source list")
    parser.add_argument("--to-path", required=False, default="out",
            help="The path where we write the output files. Defaults to `out`")
    parser.add_argument("--name-template", required=False, default="{{index}}",
            help="The template for the output file. It uses the same mappings plus the `index` variable. Defaults to {{index}}")
    parser.add_argument("--map", required=False, action='append',
            help="Map from the input column name to the output variable. Eg. first_name:firstName")
    parser.add_argument("--common-value", required=False, action='append',
            help="Template arguments that are common to all the rows and not in the input list. Eg. date:24 Feb 2023")
    parser.add_argument("--template-path", required=False, default=".",
            help="The path to the template")

    args = parser.parse_args()

    templateFilePath = Path(args.template_path, args.template)
    if not templateFilePath.exists():
        sys.exit(f"Template file not found: {templateFilePath}")
    contentTemplate = readTemplate(templateFilePath)

    csvFilePath = Path(args.from_csv)
    if not csvFilePath.exists():
        sys.exit(f"List file not found: {csvFilePath}")
    reader = CsvReader(csvFilePath)

    outPath = Path(args.to_path)
    if not outPath.exists():
        outPath.mkdir()
    fileWriter = FileWriter(outPath)

    mapping = parseMapFromString(args.map)
    commonValues = parseMapFromString(args.common_value)
    nameTemplate = args.name_template

    writer = ConsoleWriter()
    rowTemplate = RowTemplate(Template(nameTemplate, mapping), Template(contentTemplate, mapping))
    for row in reader.readNext():
        transformedRow = rowTemplate.render(row | commonValues)
        writer.write(transformedRow)
        fileWriter.write(transformedRow)

def parseMapFromString(argsString):
    return {item.split(":")[0]:item.split(":")[1] for item in argsString}

def readTemplate(templatePath):
    with open(templatePath, "r", encoding = "utf-8") as templateFile:
        return templateFile.read()

if __name__ == "__main__":
    main()
