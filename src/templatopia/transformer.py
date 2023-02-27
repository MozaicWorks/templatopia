import pystache
from TransformedRow import TransformedRow
from TemplatedRow import TemplatedRow

class Transformer:
    def __init__(self, values, mapping: dict=None):
        mapping = {} if mapping is None else mapping
        self.mappedValues = {mapping.get(key, key): value for key, value in values.items()}

    def transform(self, template):
        return pystache.render(template, self.mappedValues)

    def transformRow(self, templatedRow : TemplatedRow):
        return TransformedRow(
                self.transform(templatedRow.nameTemplate),
                self.transform(templatedRow.contentTemplate)
            )
