from pathlib import Path

from ConsoleWriter import ConsoleWriter
from FileWriter import FileWriter
from MapLoader import MapLoader
from MultiWriter import MultiWriter
from ProgressDisplay import ProgressDisplay
from TableReaderFromCsv import RowReaderFromCsv
from Template import Template
from TemplatedRow import RowTemplate
from TemplateFileReader import TemplateFileReader
from TransformProcess import TransformProcess


class RunFromArgs:
    def __init__(self, args):
        self.args=args

    def run(self):
        mapping = MapLoader(self.args.map, self.args.map_from).load()
        reader = RowReaderFromCsv(Path(self.args.from_csv))
        progressDisplay = ProgressDisplay(reader.totalRows())

        TransformProcess(
                reader=reader,

                rowTemplate=RowTemplate(
                    Template(self.args.name_template, mapping),
                    Template(
                        TemplateFileReader(
                            Path(
                                self.args.template_path,
                                self.args.template)
                            ).read(),
                        mapping
                        )),

                commonValues = MapLoader(
                    self.args.common_value,
                    self.args.common_values_from
                    ).load(),

                writer = MultiWriter(
                    ConsoleWriter(self.args.verbose),
                    FileWriter(Path(self.args.to_path))),

                progressDisplay=progressDisplay

                ).transform()
