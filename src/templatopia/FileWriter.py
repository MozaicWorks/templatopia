from pathlib import Path

from TransformedRow import TransformedRow


class FileWriter:
    def __init__(self, path):
        self.__path = path

    def write(self, transformedRow : TransformedRow):
        Path(self.__path, transformedRow.name).write_text(transformedRow.content, encoding="utf-8")
