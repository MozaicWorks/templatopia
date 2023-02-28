from csv import DictReader


class RowReaderFromCsv:
    def __init__(self, filePath):
        self.__filePath = filePath

    def readNext(self):
        with open(self.__filePath, 'r', newline=None, encoding="utf-8") as csvfile:
            csvReader = DictReader(csvfile)
            for row in csvReader:
                yield row
