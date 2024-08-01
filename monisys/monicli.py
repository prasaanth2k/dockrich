import sys
from Arguments import Arguments
from Managers.manager import Managers
import rich
from rich.console import Console
from rich.table import Table
from rich.panel import Panel


class Monisys:
    def __init__(self, args: Arguments):
        self.args = args
        if self.args.hasOptions(["--help"]):
            self.helpmessage()
    def helpmessage(self):
        console = Console()
        table = Table(show_header=False, box=None)
        table.add_column("Option", width=20)
        table.add_column("Description")
        table.add_row(" ", " ")
        table.add_row(" ", "Monisys", style="purple")
        table.add_row(" ", " ")
        table.add_row("-h, --help", "Show this help message and exit")
        panel = Panel(
            table, title="[Options]", title_align="left", border_style="bold white"
        )
        console.print(panel)


if __name__ == "__main__":
    args = Arguments(sys.argv[1:])
    Dock = Managers(args)
    test = Monisys(args)
