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
class VolumeResponse:
    def __init__(self,data:dict):
        self.driver = data.get("driver")
        self.mount_point = data.get("mount_point")
        self.name = data.get("name")
        self.type = data.get("type")
class LayersResponse:
    def __init__(self,data:dict):
        self.id = data.get("id")
        self.layer_id = data.get("layer_id")
        self.layer_order = data.get("layer_order")
class ImagehistoryResponse:
    def __init__(self,data:dict):
        self.comment = data.get("comment")
        self.created = data.get("created")
        self.created_by = data.get("created_by")
        self.id = data.get("id")
        self.size = data.get("size")
        self.tags = data.get("tags")

class Dockermountsresponse:
    def __init__(self,data:dict):
        self.destination = data.get("destination")
        self.driver = data.get("driver")
        self.id = data.get("id")
        self.mode = data.get("mode")
        self.name = data.get("name")
        self.propagation = data.get("propagation")
        self.rw = data.get("rw")
        self.source = data.get("source")
        self.type = data.get("type")
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
        
    def volumes(self) -> List[VolumeResponse]:
        try:
            docker_volumes = ["osqueryi","--json","SELECT * FROM docker_volumes;"]
            output = subprocess.run(docker_volumes,capture_output=True,check=True,text=True)
            result = json.loads(output.stdout)
            responses = [VolumeResponse(volume) for volume in result]
            return responses
        except subprocess.CalledProcessError as e:
            print(f"Error running command {e.cmd}: {e.output}")
            return []
    def layers(self) -> List[LayersResponse]:
        try:
            docker_images_layers = ["osqueryi","--json","SELECT * FROM docker_image_layers;"]
            output = subprocess.run(docker_images_layers,capture_output=True,check=True,text=True)
            result = json.loads(output.stdout)
            responses = [LayersResponse(layers) for layers in result]
            return responses
        except subprocess.CalledProcessError as e:  
            print(e.cmd)
    def imageshistory(self) -> List[ImagehistoryResponse]:
        try:
            docker_image_history = ["osqueryi","--json","SELECT * FROM docker_image_history;"]
            output = subprocess.run(docker_image_history,capture_output=True,check=True,text=True)
            result = json.loads(output.stdout)
            responses = [ImagehistoryResponse(imagehistory) for imagehistory in result]
            return responses
        except subprocess.CalledProcessError as e:
            print(e.cmd)

    def dockermounts(self) -> List[Dockermountsresponse]:
        try:
            docker_mount = ["osqueryi", "--json", "SELECT * FROM docker_container_mounts;"]
            output = subprocess.run(docker_mount, capture_output=True, check=True, text=True)
            result = json.loads(output.stdout)
            responses = [Dockermountsresponse(dockermounts) for dockermounts in result]
            return responses
        except subprocess.CalledProcessError as e:
            print(e.cmd)