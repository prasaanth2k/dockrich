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
        table.add_row("-r, --ps","Show all running docker containers")
        table.add_row("-i, --images","Show all docker images")
        table.add_row("-v, --volumes","Show all the docker volumes volumes")
        table.add_row("-l, --layers","Show all the docker image layers")
        table.add_row("-ih, --image-history","Show all image history")
        table.add_row("-dm, --docker-mounts","Show all the docker mounts")
        table.add_row("-acp,--acpi-tables","Show advanced configiration power interface")
        table.add_row("-aap,--apparmor","Show app armor profiles")
        table.add_row("-auk,--authorized_keys","List all the Authorized_Keys")
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
