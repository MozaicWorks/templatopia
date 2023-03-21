from .JsonMapLoader import JsonMapLoader
from .MapParser import MapParser


class MapLoader:
    def __init__(self, mapString, mapFile):
        self.__isFile =  not mapString
        self.__mapParser = MapParser(mapString)
        self.__jsonMapLoader = JsonMapLoader(mapFile)

    def load(self):
        return self.__jsonMapLoader.load() if self.__isFile else self.__mapParser.parse()
