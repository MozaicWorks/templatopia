import json

class JsonMapLoader:
    def __init__(self, jsonFileName):
        self.__jsonFileName = jsonFileName

    def load(self):
        return json.load(open(self.__jsonFileName, encoding="utf-8"))
