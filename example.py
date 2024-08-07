from monisys.Managers.dockermanager import Dockermanage
from monisys.Managers.essentialsmanager import EssentialsManager
docker = Dockermanage()
essentials = EssentialsManager()
ps = docker.ps()
for i in ps:
    print(i.id)

images = docker.images()
for i in images:
    print(i.created)

volumes = docker.volumes()
for i in volumes:
    print(i.driver)

layers = docker.layers()
for i in layers:
    print(i.layer_id)

imagehistory = docker.imageshistory()
for i in imagehistory:
    print(i.created_by)

dockermounts = docker.dockermounts()
for i in dockermounts:
    print(i.propagation)

acpi = essentials.acpi_tables()
for i in acpi:
    print(i.size)

apparmot = essentials.apparmor_profiles()
for i in apparmot:
    print(i.sha1)