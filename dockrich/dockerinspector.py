import subprocess
import json


class Response:
    def __init__(self, data: dict):
        self.Id = data.get("Id")
        self.Created = data.get("Created")
        self.Path = data.get("Path")
        self.Args = data.get("Args")
        self.State = data.get("State")
        self.Image = data.get("Image")
        self.ResolvConfPath = data.get("ResolvConfPath")
        self.HostnamePath = data.get("HostnamePath")
        self.HostsPath = data.get("HostsPath")
        self.LogPath = data.get("LogPath")
        self.Name = data.get("Name")
        self.RestartCount = data.get("RestartCount")
        self.Driver = data.get("Driver")
        self.Platform = data.get("Platform")
        self.MountLabel = data.get("MountLabel")
        self.ProcessLabel = data.get("ProcessLabel")
        self.AppArmorProfile = data.get("AppArmorProfile")
        self.ExecIDs = data.get("ExecIDs")
        self.HostConfig = data.get("HostConfig")
        self.CapAdd = data.get("CapAdd")
        self.CapDrop = data.get("CapDrop")
        self.CgroupnsMode = data.get("CgroupnsMode")
        self.Dns = data.get("Dns")
        self.DnsOptions = data.get("DnsOptions")
        self.DnsSearch = data.get("DnsSearch")
        self.ExtraHosts = data.get("ExtraHosts")
        self.GroupAdd = data.get("GroupAdd")
        self.IpcMode = data.get("IpcMode")
        self.Cgroup = data.get("Cgroup")
        self.Links = data.get("Links")
        self.OomScoreAdj = data.get("OomScoreAdj")
        self.PidMode = data.get("PidMode")
        self.Privileged = data.get("Privileged")
        self.PublishAllPorts = data.get("PublishAllPorts")
        self.ReadonlyRootfs = data.get("ReadonlyRootfs")
        self.SecurityOpt = data.get("SecurityOpt")
        self.UTSMode = data.get("UTSMode")
        self.UsernsMode = data.get("UsernsMode")
        self.ShmSize = data.get("ShmSize")
        self.Runtime = data.get("Runtime")
        self.Isolation = data.get("Isolation")
        self.CpuShares = data.get("CpuShares")
        self.Memory = data.get("Memory")
        self.NanoCpus = data.get("NanoCpus")
        self.CgroupParent = data.get("CgroupParent")
        self.BlkioWeight = data.get("BlkioWeight")
        self.BlkioWeightDevice = data.get("BlkioWeightDevice")
        self.BlkioDeviceReadBps = data.get("BlkioDeviceReadBps")
        self.BlkioDeviceWriteBps = data.get("BlkioDeviceWriteBps")
        self.BlkioDeviceReadIOps = data.get("BlkioDeviceReadIOps")
        self.BlkioDeviceWriteIOps = data.get("BlkioDeviceWriteIOps")
        self.CpuPeriod = data.get("CpuPeriod")
        self.CpuQuota = data.get("CpuQuota")
        self.CpuRealtimePeriod = data.get("CpuRealtimePeriod")
        self.CpuRealtimeRuntime = data.get("CpuRealtimeRuntime")
        self.CpusetCpus = data.get("CpusetCpus")
        self.CpusetMems = data.get("CpusetMems")
        self.Devices = data.get("Devices")
        self.DeviceCgroupRules = data.get("DeviceCgroupRules")
        self.DeviceRequests = data.get("DeviceRequests")
        self.MemoryReservation = data.get("MemoryReservation")
        self.MemorySwap = data.get("MemorySwap")
        self.MemorySwappiness = data.get("MemorySwappiness")
        self.OomKillDisable = data.get("OomKillDisable")
        self.PidsLimit = data.get("PidsLimit")
        self.Ulimits = data.get("Ulimits")
        self.CpuCount = data.get("CpuCount")
        self.CpuPercent = data.get("CpuPercent")
        self.IOMaximumIOps = data.get("IOMaximumIOps")
        self.IOMaximumBandwidth = data.get("IOMaximumBandwidth")
        self.MaskedPaths = data.get("MaskedPaths")
        self.ReadonlyPaths = data.get("ReadonlyPaths")
        self.GraphDriver = data.get("GraphDriver")
        self.Mounts = data.get("Mounts")
        self.Config = data.get("Config")
        self.NetworkSettings = data.get("NetworkSettings")

    def __repr__(self) -> str:
        return f"<Response {self.__dict__}>"


class Dockerinspector:
    def __init__(self, containerid_or_name: str):
        self.containerid_or_name = containerid_or_name

    def getvalues(self) -> Response:
        docker_command = [
            "docker", "inspect", "--size", "--format", '{{json .}}', self.containerid_or_name
        ]
        try:
            output = subprocess.run(
                docker_command, capture_output=True, check=True, text=True
            )
            value = json.loads(output.stdout)  # The output is already in JSON format
            return Response(value)
        except subprocess.CalledProcessError as e:
            raise Exception(f"Error: {e.stderr.strip()}")
