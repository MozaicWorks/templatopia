from csv import DictReader

class CsvReader:
    def __init__(self, filePath):
        self.__filePath = filePath

    def readNext(self):
         with open(self.__filePath, 'r', newline=None) as csvfile:
            csvReader = DictReader(csvfile)
            for row in csvReader:
                yield row
