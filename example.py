from monisys.Managers.dockermanager import Dockermanage

docker = Dockermanage()

vaule = docker.ps()
for d in vaule:
    print(d.id)