import argparse
from pathlib import Path
import sys
import csv

def main():
    parser = argparse.ArgumentParser(
                    prog = 'templatopia',
                    description = 'Creates files from a template file and a table. The templating language use is Mustache.',
    )
    parser.add_argument("--template", required=True, help="The name of the template file. Eg. template.svg, template.eml")
    parser.add_argument("--from-csv", required=False, help="The csv file containing the source list")
    parser.add_argument("--to-path", required=False, default="out", help="The path where we write the output files. Defaults to `out`")
    parser.add_argument("--name-template", required=False, default="{{index}}", help="The template for the output file. It uses the same mappings plus the `index` variable. Defaults to {{index}}")
    parser.add_argument("--out-ext", required=False, help="The extension of the output file. Defaults to the extension of the template")
    parser.add_argument("--map", required=False, action='append', help="Map from the input column name to the output variable. Eg. first_name:firstName")
    parser.add_argument("--template-path", required=False, default=".", help="The path to the template")
    
    args = parser.parse_args()

    templateFilePath = Path(args.template_path, args.template)
    if(not templateFilePath.exists()):
        sys.exit("Template file not found: {templateFilePath}".format(templateFilePath=templateFilePath))

    csvFilePath = Path(args.from_csv)
    if(not csvFilePath.exists()):
        sys.exit("List file not found: {csvFilePath}".format(csvFilePath=csvFilePath))

    outPath = Path(args.to_path)
    if(not outPath.exists()):
        outPath.mkdir()

    mappingArgs = args.map
    mapping = {item.split(":")[0]:item.split(":")[1] for item in mappingArgs}

    from TableReaderFromCsv import CsvReader
    reader = CsvReader(csvFilePath)
    for row in reader.readNext():
        from transformer import transform
        template = readTemplate(templateFilePath)
        transformed = transform(template, row, mapping)
        print(transformed)

def readTemplate(templatePath):
    with(open(templatePath, "r") as templateFile):
        return templateFile.read()

if __name__ == "__main__":
    main()
