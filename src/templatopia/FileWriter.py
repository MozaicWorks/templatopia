from pathlib import Path

from .TransformedRow import TransformedRow


class FileWriter:
    def __init__(self, path):
        self.__path = path

    def __ensurePathExists(self):
        if not self.__path.exists():
            self.__path.mkdir()

    def write(self, transformedRow : TransformedRow):
        self.__ensurePathExists()
        file = Path(self.__path, transformedRow.name)
        assert transformedRow.name, "empty name"
        assert file.is_file(), f"{file}"
        Path(self.__path, transformedRow.name).write_text(transformedRow.content, encoding="utf-8")
