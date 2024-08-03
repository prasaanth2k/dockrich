import subprocess
import json


class Dockermanagecli:

    def ps(self):
        try:
            docker_containers = ["osqueryi","--json","SELECT * FROM docker_containers;",]
            output = subprocess.run(docker_containers, capture_output=True, check=True)
            result = json.loads(output.stdout)
            return result
        except subprocess.CalledProcessError as e:
            print(e.cmd)

    def images(self):
        try:
            docker_images = ["osqueryi", "--json", "SELECT * FROM docker_images;"]
            output = subprocess.run(docker_images, capture_output=True, check=True, text=True)
            result = json.loads(output.stdout)
            return result
        except subprocess.CalledProcessError as e:
            print(e.cmd)
    def docker_volumes(self):
        try:
            docker_volumes = ["osqueryi","--json","SELECT * FROM docker_volumes;"]
            output = subprocess.run(docker_volumes,capture_output=True,check=True,text=True)
            result = json.loads(output.stdout)
            return result
        except subprocess.CalledProcessError as e:
            print(e.cmd)