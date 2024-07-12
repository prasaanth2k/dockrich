import sys
from lib.dockrich_helper import DockrichHelper

dr = DockrichHelper()


def has_args():
    return str(sys.argv[1])


def display_help():
    print("Usage: dockrich [OPTION]...")
    print("With this you can able to pretty you docker outputs")
    print("Mandatory arguments to long options are mandatory for short options too.\n")
    print("  -rl, --running_containers to print all running containers with [Container ID] [Name] [Image] [State] [Networks] [Commands] [CreatedAt]")
    print("  -ti, --list_true_images to list images without none tag and none name with [Repository] [Tag] [Container ID] [Created Since] [Size] ")
    print("  -cp, --running_ports to list running container ports [Container ID] [Ports]")
def main():
    args_count = len(sys.argv)
    if args_count <= 1:
        display_help()
    else:
        if has_args() == "-h":
            display_help()
        elif has_args() == "-ti":
            dr.list_true_without_none()
        elif has_args() == "-cp":
            dr.list_container_ports()
        elif has_args() == "-rl":
            dr.list_running_containers()
        else:
            display_help()


if __name__ == "__main__":
    main()
