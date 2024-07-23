from dockrich.dockmanager import Dockermanager

DM = Dockermanager()

DM.list_container_ports()
DM.list_networks()
DM.list_true_without_none()
DM.run_container(imagename="kalilinux/kali-rolling",imagetag="latest",command="tail -f /dev/null")
