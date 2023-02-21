class ConsoleWriter:
    def write(self, fileName, fileContent):
        print("{fileName}: {fileContent}".format(fileName=fileName, fileContent=fileContent))
