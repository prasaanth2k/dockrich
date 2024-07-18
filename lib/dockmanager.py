import subprocess
from rich.console import Console
from rich.table import Table
import shlex
from time import sleep
from rich import print
import secrets

imagenames = secrets.token_urlsafe(8)
class Dockermanager:
    def __init__(self):
        pass
    def build(self, tags="latest", name="imagenames", path='.'):
        try:
            dockercommand = f"docker build -t {name}:{tags} {path}"
            result = subprocess.run(dockercommand, shell=True, capture_output=True, text=True, check=True)
            print(result.stdout)
            print(result.stderr)
        except subprocess.CalledProcessError as e:
            print(f"[bold red] {e.stderr} [/bold red]")
    def stop_all_running_containers(self):
        try:
            dockercommand = "docker stop $(docker ps -a -q)"
            result = subprocess.run(dockercommand,shell=True,capture_output=True,text=True,check=True)
            container_ids = result.stdout.splitlines()
            for i in container_ids:
                print(f"[green bold]*[/green bold] [purple]{i} Container Stopped 📦 [/purple]")
                sleep(2)
        except subprocess.CalledProcessError as e:
            if e.returncode == 1:
                print(f"[bold red] {e} [/bold red]")