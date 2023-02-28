class MapParser:
    def __init__(self, argsString : str):
        self.argsString = argsString

    def parse(self):
        return {item.split(":")[0]:item.split(":")[1] for item in self.argsString}
