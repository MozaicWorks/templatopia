import pystache

class Transformer:
    def __init__(self, values, mapping: dict=None):
        mapping = {} if mapping is None else mapping
        self.mappedValues = {mapping.get(key, key): value for key, value in values.items()}

    def transform(self, template):
        return pystache.render(template, self.mappedValues)
