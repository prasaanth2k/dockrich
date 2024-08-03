import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from monisys.Managers.Arguments import Arguments
from monisys.Managers.manager import Managers
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

class Monisys:
    def __init__(self, args: Arguments):
        self.args = args
        if self.args.hasOptions(["--help"]) or self.args.hasOptions(["-h"]):
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
        table.add_row("--ps","Show all running containers")
        panel = Panel(
            table, title="[Options]", title_align="left", border_style="bold white"
        )
        console.print(panel)

def main():
    args = Arguments(sys.argv[1:])
    Dock = Managers(args)
    test = Monisys(args)

if __name__ == "__main__":
    main()
