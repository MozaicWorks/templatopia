import rich


class ProgressDisplay:
    def __init__(self, totalRowCount: int):
        self.totalRowCount=totalRowCount
        self.successful = 0

    def progress(self, row, currentIndex):
        rich.print(f"{currentIndex}/{self.totalRowCount}: {row}")

    def success(self):
        self.successful += 1
        rich.print("[green bold]Success![/]\n")

    def error(self, error):
        rich.print(f"[red bold]Error[/]: {error}\n")

    def summary(self):
        rich.print(f"[bold]Total: {self.totalRowCount}[/] [green bold]Successful: {self.successful}[/] [red bold]Failed: {self.totalRowCount - self.successful}[/]")
