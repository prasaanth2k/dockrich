from monisys.Managers.dockermanager import Dockermanage

docker = Dockermanage()

vaule = docker.images()
for d in vaule:
    print(d.id)