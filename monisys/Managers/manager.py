from monisys.Managers.Arguments import Arguments
from monisys.Managers.dockermanager import Dockermanage
from .dockermanager import Dockermanage

Dock = Dockermanage()


class Managers:
    def __init__(self, args: Arguments):
        self.args = args

        if self.args.hasOptions(["--ps"]):
            responses = Dock.ps()
            for rss in responses:
                print(rss.pid)
