from TemplatedRow import TemplatedRow
from transformer import Transformer


class TransformProcess:

    def __init__(self, mapping, commonValues):
        self.mapping = mapping
        self.commonValues = commonValues

    def next(self, rowReader, templatedRow : TemplatedRow):
        for row in rowReader.readNext():
            transformer = Transformer(row | self.commonValues, self.mapping)
            yield transformer.transformRow(templatedRow)
