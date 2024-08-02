import subprocess
import json
from typing import List

class ContainerResponse:
    def __init__(self, data: dict):
        self.cgroup_namespace = data.get("cgroup_namespace")
        self.command = data.get("command")
        self.config_entrypoint = data.get("config_entrypoint")
        self.created = data.get("created")
        self.env_variables = data.get("env_variables")
        self.finished_at = data.get("finished_at")
        self.id = data.get("id")
        self.image = data.get("image")
        self.image_id = data.get("image_id")
        self.ipc_namespace = data.get("ipc_namespace")
        self.mnt_namespace = data.get("mnt_namespace")
        self.name = data.get("name")
        self.net_namespace = data.get("net_namespace")
        self.path = data.get("path")
        self.pid = data.get("pid")
        self.pid_namespace = data.get("pid_namespace")
        self.privileged = data.get("privileged")
        self.readonly_rootfs = data.get("readonly_rootfs")
        self.security_options = data.get("security_options")
        self.started_at = data.get("started_at")
        self.state = data.get("state")
        self.status = data.get("status")
        self.user_namespace = data.get("user_namespace")
        self.uts_namespace = data.get("uts_namespace")

    def __repr__(self) -> str:  
        return f"<ContainerResponse {self.__dict__}>"

class ImageResponse:
    def __init__(self, data: dict):
        self.id = data.get("id")
        self.created = data.get("created")
        self.size_bytes = data.get("size_bytes")
        self.tags = data.get("tags")
    
    def __repr__(self) -> str:
        return f"<ImageResponse {self.__dict__}>"

class Dockermanage:
    def ps(self) -> List[ContainerResponse]:
        try:
            docker_containers = ["osqueryi", "--json", "SELECT * FROM docker_containers;"]
            output = subprocess.run(docker_containers, capture_output=True, check=True, text=True)
            result = json.loads(output.stdout)
            responses = [ContainerResponse(container) for container in result]
            return responses
        except subprocess.CalledProcessError as e:
            print(f"Error running command {e.cmd}: {e.output}")
            return []

    def images(self) -> List[ImageResponse]:
        try:
            docker_images = ["osqueryi", "--json", "SELECT * FROM docker_images;"]
            output = subprocess.run(docker_images, capture_output=True, check=True, text=True)
            result = json.loads(output.stdout)
            responses = [ImageResponse(image) for image in result]
            return responses
        except subprocess.CalledProcessError as e:
            print(f"Error running command {e.cmd}: {e.output}")
            return []