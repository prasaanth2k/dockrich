import argparse
from lib.dockrich_helper import DockrichHelper
from lib.dockmanager import Dockermanager
from lib.dockcompose import load_json


def main():
    parser = argparse.ArgumentParser(description="With this you can able to pretty you docker outputs")
    parser.add_argument("-rl","--running_containers",action="store_true",help="Print all running containers",)
    parser.add_argument("-ti","--list_true_images",action="store_true",help="List images without none tag and none name",)
    parser.add_argument("-cp","--running_ports",action="store_true",help="List running container ports",)
    parser.add_argument("-nl", "--list_networks", action="store_true", help="List all the networks")
    parser.add_argument("-sac","--stop_all_containers",action="store_true",help="Stop all running containers",)
    parser.add_argument("-cf", "--composer_file", help="Input compose file")
    parser.add_argument("-b", "--build", action="store_true", help="Build a Docker image")
    parser.add_argument("--image_name", help="Name of the Docker image")
    parser.add_argument("--tags", default="latest", help="Tags for the Docker image")
    parser.add_argument("--path", help="Path to the Dockerfile directory")
    args = parser.parse_args()

    dr = DockrichHelper()
    dm = Dockermanager()

    if args.running_containers:
        dr.list_running_containers()
    elif args.list_true_images:
        dr.list_true_without_none()
    elif args.running_ports:
        dr.list_container_ports()
    elif args.list_networks:
        dr.list_networks()
    elif args.stop_all_containers:
        dm.stop_all_running_containers()
    elif args.build:
        if not (args.image_name and args.path):
            parser.error("--build requires --image_name and --path arguments.")
        else:
            dm.build(tags=args.tags, name=args.image_name, path=args.path)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
