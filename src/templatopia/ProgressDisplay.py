import rich


class ProgressDisplay:
    def __init__(self, totalRowCount: int):
        self.totalRowCount=totalRowCount

    def progress(self, row, currentIndex):
        rich.print(f"{currentIndex}/{self.totalRowCount}: {row}")

    def success(self):
        rich.print("[green bold]Success![/]\n")

    def error(self, error):
        rich.print(f"[red bold]Error[/]: {error}\n")
