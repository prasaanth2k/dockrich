# lib/dockrich_helper.py
import subprocess
from rich.console import Console
from rich.table import Table
import shlex


class DockrichHelper:
    def __init__(self):
        pass

    def list_running_containers(self):
        try:
            # Run the Docker command to list running containers with networks and command
            out = subprocess.run(
                [
                    "docker",
                    "ps",
                    "--format",
                    "{{.ID}} {{.Image}} {{.Names}} {{.State}} {{.Networks}} {{.Command}} {{.CreatedAt}}",
                ],
                capture_output=True,
                text=True,
                check=True,
            )

            # Parse the output into a table using rich
            console = Console()
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Container ID", style="cyan")
            table.add_column("Name", style="yellow")
            table.add_column("Image", style="bold green")
            table.add_column("State", style="green")
            table.add_column("Networks", style="red")
            table.add_column("Command", style="blue")
            table.add_column("CreatedAt", style="purple")

            # Process each line of Docker output
            for line in out.stdout.splitlines():
                parts = shlex.split(line)
                container_id, name, image, state, networks, command, createdat = (
                    parts[0],
                    parts[1],
                    parts[2],
                    parts[3],
                    parts[4],
                    parts[5],
                    " ".join(parts[6:]),
                )
                table.add_row(
                    container_id, name, image, state, networks, command, createdat
                )

            console.print(table)

        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

    def list_container_ports(self):
        try:
            containers = subprocess.run(
                ["docker", "ps", "--format", "{{.ID}}"],
                capture_output=True,
                text=True,
                check=True,
            )
            out = subprocess.run(
                ["docker", "ps", "--format", "{{.Ports}}"],
                capture_output=True,
                text=True,
                check=True,
            )
            console = Console()
            table = Table(
                show_header=True, header_style="bold magenta", show_lines=True
            )
            table.add_column("Container ID", style="green")
            table.add_column("Ports", style="cyan")
            container_ids = containers.stdout.strip().split("\n")
            ports_list = out.stdout.strip().split("\n")
            for container_id, ports in zip(container_ids, ports_list):
                table.add_row(container_id, ports)
            console.print(table)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
