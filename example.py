from monisys.Managers.dockermanager import Dockermanage

docker = Dockermanage()

ps = docker.ps()
for i in ps:
    print(i.id)

images = docker.images()
for i in images:
    print(i.created)

volumes = docker.volumes()
for i in volumes:
    print(i.driver)