import subprocess
import json


class Response:
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
        return f"<Response>{self.__dict__}"


class Dockermanage:

    def ps(self) -> list[Response]:
        docker_containers = "osqueryi --json 'SELECT * FROM docker_containers;'"
        output = subprocess.run(
            docker_containers, shell=True, capture_output=True, check=True
        )
        result = json.loads(output.stdout)
        responses = [Response(container) for container in result]
        return responses