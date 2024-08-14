from monisys.Managers.systeminfocli import SystemInfoCLI
from monisys.Managers.Arguments import Arguments
system = SystemInfoCLI()

class Managers:
    def __init__(self,args:Arguments):
        self.args = args

        if self.args.hasOptions(["--cpulive"]) or self.args.hasOptions(["-cl"]):
            system.display_uptime()
        if self.args.hasOptions(["--kernal-info"]) or self.args.hasOptions(["-ki"]):
            system.display_kernel_info()