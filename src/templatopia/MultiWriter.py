from TransformedRow import TransformedRow


class MultiWriter:
    def __init__(self, *writers):
        self.writers = writers

    def write(self, row:TransformedRow):
        for writer in self.writers:
            writer.write(row)
