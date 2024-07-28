from dockrich.dockerinspector import Dockerinspector
from dockrich.dockerhistory import Dockerhistory
from dockrich.dockerstats import Dockerstats
from dockrich.dockermanage import Dockermanage

inspect = Dockerinspector(containerid_or_name="hopeful_wing")
images = Dockerhistory(image_name="prasaanthdjango")
status = Dockerstats(containerid_or_name="debian_container")

values = inspect.getvalues()
print(values.HostConfig['IpcMode'])

for image in images.getvalues():
    print(image.Size)

s = status.getstats()
print(s.BlockIO)

ps = Dockermanage(containerid_or_name="debian_container")

output = ps.ps()
print(output.LocalVolumes)
