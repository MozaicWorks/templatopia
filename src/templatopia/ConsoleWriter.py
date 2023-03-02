from TransformedRow import TransformedRow
from rich import print


class ConsoleWriter:
    def write(self, transformedRow : TransformedRow):
        print(f"[bold]{transformedRow.name}:[/bold]")
        print(f"{transformedRow.content}")
