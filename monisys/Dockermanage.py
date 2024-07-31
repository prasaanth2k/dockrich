import subprocess
import json
from Arguments import Arguments
class Dockermanage:
    def __init__(self,args:Arguments):
        self.args = args

        if self.args.hasOptions(['--ps']):
            print(self.ps())

    def ps(self):
        docker_containers = "osqueryi --json 'SELECT * FROM docker_containers;'"
        output = subprocess.run(docker_containers, shell=True, capture_output=True, check=True)
        result = json.loads
        return json.loads(output.stdout)