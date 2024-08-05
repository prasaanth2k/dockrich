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
        
        if self.args.hasOptions(["--ps"]) or self.args.hasOptions(["-r"]):
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
        
        if self.args.hasOptions(["--images"]) or self.args.hasOptions(["-i"]):
            images = Dock.images()
            if images:
                table = Table(title="Docker images")
                table.add_column("ID", justify="left", style="cyan")
                table.add_column("Created", justify="left", style="magenta")
                table.add_column("Size (GB)", justify="left", style="green")
                table.add_column("Tags", justify="left", style="yellow")
                for image in images:
                    size_gb = int(image['size_bytes']) / (1024**3)  # Convert bytes to GB
                    size_gb_str = f"{size_gb:.2f} GB"  # Format as string with 2 decimal places

                    table.add_row(
                        image['id'],
                        image['created'],
                        size_gb_str,
                        ", ".join(image['tags']) if isinstance(image['tags'], list) else image['tags']
                    )
                console.print(table)
            else:
                print("[bold white][*] No Images available[/bold white]")
        
        if self.args.hasOptions(["--volumes"]) or self.args.hasOptions(["-v"]):
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
                print("[bold white][*] No volumes [/bold white]")
        
        if self.args.hasOptions(["-l"]) or self.args.hasOptions(["--layers"]):
            layers = Dock.docker_image_layers()
            if layers:
                table = Table(title="Image layers")
                table.add_column("ID", justify="left", style="cyan")
                table.add_column("Layer ID", justify="left", style="magenta")
                table.add_column("Layer Order", justify="left", style="green")
                for layer in layers:
                    table.add_row(
                        layer['id'],
                        layer['layer_id'],
                        layer['layer_order']
                    )
                console.print(table)
            else:
                print("[bold white][*] No image layers available[/bold white]")
        
        if self.args.hasOptions(["-ih"]) or self.args.hasOptions(["--image-history"]):
            image_historys = Dock.docker_image_history()
            if image_historys:
                table = Table(title="Image History")
                table.add_column("Comment", justify="left", style="cyan")
                table.add_column("Created", justify="left", style="magenta")
                # table.add_column("Created_By", justify="left", style="green")
                table.add_column("ID",justify="left",style="cyan")
                table.add_column("Size",justify="left",style="magenta")
                table.add_column("Tags",justify="left",style="cyan")
                for historys in image_historys:
                    table.add_row(
                        historys['comment'],
                        historys['created'],
                        # historys['created_by'],
                        historys['id'],
                        historys['size'],
                        historys['tags']
                    )
                console.print(table)
            else:
                print("[bold white][*] No image history available[/bold white]")

        if self.args.hasOptions(['-dm']) or self.args.hasOptions(['--docker-mounts']):
            docker_mounts = Dock.docker_mounts()
            if docker_mounts:
                table = Table(title="Docker mounts")
                table.add_column("Destination", justify="left", style="cyan")
                table.add_column("Driver", justify="left", style="magenta")
                table.add_column("ID", justify="left", style="cyan")
                table.add_column("Mode", justify="left", style="magenta")
                table.add_column("Name", justify="left", style="cyan")
                table.add_column("Propagation", justify="left", style="cyan")
                table.add_column("RW", justify="left", style="magenta")
                table.add_column("Source", justify="left", style="cyan")
                table.add_column("Type", justify="left", style="cyan")
                for docker_mount in docker_mounts:
                    table.add_row(
                        docker_mount['destination'],
                        docker_mount['driver'],
                        docker_mount['id'],
                        docker_mount['mode'],
                        docker_mount['name'],
                        docker_mount['propagation'],
                        docker_mount['rw'],
                        docker_mount['source'],
                        docker_mount['type']
                    )
                console.print(table)
            else:
                console.print("[bold white][*] No mounts available[/bold white]")