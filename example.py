# from dockrich.dockmanager import Dockermanager

# DM = Dockermanager()

# DM.list_container_ports()
# DM.list_networks()
# DM.list_true_without_none()
# DM.run_container(imagename="kalilinux/kali-rolling",imagetag="latest",command="tail -f /dev/null")
# DM.start_container(containername="minio")
# DM.list_all_container()

from dockrich.dockerinspector import Dockerinspector

m = Dockerinspector(containerid="40465720184c")

instance  = m.getvalues()
print(instance.Name)