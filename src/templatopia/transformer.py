import pystache


class Template:
    def __init__(self, template, mapping: dict=None):
        self.template = template
        self.mapping = {} if mapping is None else mapping

    def __mapValues(self, values):
        return {self.mapping.get(key, key): value for key, value in values.items()}

    def render(self, values):
        return pystache.render(self.template, self.__mapValues(values))
