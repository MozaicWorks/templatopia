from transformer import Transformer

class TransformProcess:

    def __init__(self, mapping, commonValues):
        self.mapping = mapping
        self.commonValues = commonValues

    def run(self, reader, writer, template, fileNameTemplate):
        for row in reader.readNext():
            self.__doTransform(row | self.commonValues, writer, template, fileNameTemplate)

    def __doTransform(self, values, writer, template, fileNameTemplate):
        theTransformer = Transformer(values, self.mapping)
        transformed = theTransformer.transform(template)
        fileName = theTransformer.transform(fileNameTemplate)
        writer.write(fileName, transformed)
