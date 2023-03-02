from csv import DictReader


class RowReaderFromCsv:
    def __init__(self, filePath):
        self.__filePath = filePath

    def totalRows(self):
        with open(self.__filePath, 'r', encoding="utf-8") as csvfile:
            lines = sum(1 for line in csvfile)
            # Ignore the header line which we assume exists
            return lines - 1


    def readNext(self):
        with open(self.__filePath, 'r', newline=None, encoding="utf-8") as csvfile:
            csvReader = DictReader(csvfile)
            rowIndex = 0
            for row in csvReader:
                rowIndex += 1
                yield row, rowIndex
