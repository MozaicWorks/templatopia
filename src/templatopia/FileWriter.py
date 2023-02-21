from pathlib import Path

class FileWriter:
    def __init__(self, path):
        self.__path = path

    def write(self, fileName, fileContent):
        Path(self.__path, fileName).write_text(fileContent)

