class TransformProcess:
    def __init__(self, reader, rowTemplate, commonValues, writer, progressDisplay):
        self.reader = reader
        self.rowTemplate = rowTemplate
        self.commonValues = commonValues
        self.writer = writer
        self.progressDisplay = progressDisplay

    def transform(self):
        for row, rowIndex in self.reader.readNext():
            self.progressDisplay.progress(row, rowIndex)
            try:
                transformedRow = self.rowTemplate.render(row | self.commonValues)
                self.writer.write(transformedRow)
                self.progressDisplay.success()
            except Exception as e:
                self.progressDisplay.error(e)

        self.progressDisplay.summary()
