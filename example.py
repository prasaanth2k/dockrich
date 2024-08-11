from monisys.Managers.dockermanager import Dockermanage
from monisys.Managers.essentialsmanager import EssentialsManager
from monisys.Managers.systemresourses import Cpuinforesponse , CpuidResponse

# Create instances of the managers
cpuinfo = Cpuinforesponse()
cpuid = CpuidResponse()
docker = Dockermanage()
essentials = EssentialsManager()

# docker_images = docker.images()
# for image in docker_images:
#     print(image.id)

print(cpuinfo.manufacturer)
