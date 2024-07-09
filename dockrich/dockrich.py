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
    args = parser.parse_args()

    dockrichobj = DockrichHelper()

    if args.all_running_containers:
        dockrichobj.list_running_containers()
    elif args.running_ports:
        dockrichobj.list_container_ports()

if __name__ == "__main__":
    main()
