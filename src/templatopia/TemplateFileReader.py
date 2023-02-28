from pathlib import Path

class TemplateFileReader:
    def __init__(self, path : Path):
        self.path = path

    def read(self) -> str:
        with open(self.path, "r", encoding = "utf-8") as templateFile:
            return templateFile.read()
