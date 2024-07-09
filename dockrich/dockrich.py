# dockrich/dockrich.py

import argparse
import sys
from lib.dockrich_helper import DockrichHelper

def main():
    parser = argparse.ArgumentParser(prog="Dockrich")
    parser.add_argument(
        "-all", "--all_running_containers", action="store_true", help="List running Docker containers"
    )
    parser.add_argument(
        "-cp",
        "--running_ports",
        action="store_true",
        help="List running Docker container ports",
    )
    parser.add_argument("-ti","--list_true_images",action="store_true",help="List the images with out None")
    args = parser.parse_args()

    dockrichobj = DockrichHelper()

    if args.all_running_containers:
        dockrichobj.list_running_containers()
    elif args.running_ports:
        dockrichobj.list_container_ports()
    elif args.list_true_images:
        dockrichobj.list_true_without_none()

if __name__ == "__main__":
    main()
