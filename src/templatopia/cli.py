import argparse
from pathlib import Path

from ConsoleWriter import ConsoleWriter
from FileWriter import FileWriter
from MapParser import MapParser
from MultiWriter import MultiWriter
from ProgressDisplay import ProgressDisplay
from TableReaderFromCsv import RowReaderFromCsv
from Template import Template
from TemplatedRow import RowTemplate
from TemplateFileReader import TemplateFileReader


def main():
    parser = argparse.ArgumentParser(
                    prog = 'templatopia',
                    description = 'Creates files from a template and a list, using Mustache'
    )
    parser.add_argument("--template", required=True,
            help="The name of the template file. Eg. template.svg, template.eml")
    parser.add_argument("--from-csv", required=False,
            help="The csv file containing the source list")
    parser.add_argument("--to-path", required=False, default="out",
            help="The path where we write the output files. Defaults to `out`")
    parser.add_argument("--name-template", required=True,
            help="The template for the output file. It uses the same mappings")
    parser.add_argument("--map", required=False, action='append',
            help="Map from the input column name to the output variable. Eg. first_name:firstName")
    parser.add_argument("--common-value", required=False, action='append',
            help="Template arguments common to all rows. Eg. date:24 Feb 2023")
    parser.add_argument("--template-path", required=False, default=".",
            help="The path to the template")

    args = parser.parse_args()

    mapping = MapParser(args.map).parse()
    commonValues = MapParser(args.common_value).parse()

    contentTemplateReader = TemplateFileReader(Path(args.template_path, args.template))

    rowTemplate = RowTemplate(
            Template(args.name_template, mapping),
            Template(contentTemplateReader.read(), mapping)
            )

    reader = RowReaderFromCsv(Path(args.from_csv))
    multiWriter = MultiWriter(ConsoleWriter(), FileWriter(Path(args.to_path)))

    progressDisplay = ProgressDisplay(reader.totalRows())

    for row, rowIndex in reader.readNext():
        progressDisplay.progress(row, rowIndex)
        try:
            transformedRow = rowTemplate.render(row | commonValues)
            multiWriter.write(transformedRow)
            progressDisplay.success()
        except Exception as e:
            progressDisplay.error(e)

    progressDisplay.summary()

if __name__ == "__main__":
    main()
