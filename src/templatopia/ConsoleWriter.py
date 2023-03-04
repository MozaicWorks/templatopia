from TransformedRow import TransformedRow
from rich import print


class ConsoleWriter:
    def __init__(self, verbose):
        self.verbose = verbose

    def write(self, transformedRow : TransformedRow):
        if self.verbose: 
            print(f"[bold]{transformedRow.name}:[/bold]")
            print(f"{transformedRow.content}")
