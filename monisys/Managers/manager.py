from monisys.Managers.Arguments import Arguments
from monisys.Managers.dockerclimanager import Dockermanagecli
from rich.console import Console
from rich.table import Table
from rich import print
import math
Dock = Dockermanagecli()
console = Console()
class Managers:
    def __init__(self, args: Arguments):
        self.args = args
        if self.args.hasOptions(["--ps"]):
            containers = Dock.ps()
            if containers:
                table = Table(title="Running Docker Containers")
                table.add_column("ID", justify="left", style="cyan")
                table.add_column("Name", justify="left", style="magenta")
                table.add_column("Image", justify="left", style="green")
                table.add_column("Command", justify="left", style="yellow")
                table.add_column("Status", justify="left", style="blue")
                table.add_column("Created", justify="left", style="white")
                for container in containers:
                    table.add_row(
                        container['id'],
                        container['name'],
                        container['image'],
                        container['command'],
                        container['status'],
                        container['created']
                    )
                console.print(table)
            else:
                print("[bold white][*] No running containers [/bold white]")
        if self.args.hasOptions(["--images"]):
            images = Dock.images()
            if images:
                table = Table(title="Docker images")
                table.add_column("ID", justify="left", style="cyan")
                table.add_column("created", justify="left", style="magenta")
                table.add_column("size_bytes", justify="left", style="green")
                table.add_column("tags", justify="left", style="yellow")
                for image in images:
                    size_gb = int(image['size_bytes']) / (1024**3)  # Convert bytes to GB
                    size_gb_str = f"{size_gb:.2f} GB"  # Format as string with 2 decimal places

                    table.add_row(
                        image['id'],
                        image['created'],
                        size_gb_str,
                        ", ".join(image['tags']) if isinstance(image['tags'], list) else image['tags'])
                console.print(table)
            else:
                print("[bold white][*] No Images available")

        if self.args.hasOptions(["--volumes"]):
            volumes = Dock.docker_volumes()
            if volumes:
                table = Table(title="Docker volumes")
                table.add_column("Driver", justify="left", style="cyan")
                table.add_column("Mounted Point", justify="left", style="magenta")
                table.add_column("Name", justify="left", style="green")
                table.add_column("Type", justify="left", style="yellow")
                for volume in volumes:
                    table.add_row(
                        volume['driver'],
                        volume['mount_point'],
                        volume['name'],
                        volume['type']
                    )
                    console.print(table)
            else:
                print("[bold white][*] No running containers [/bold white]")