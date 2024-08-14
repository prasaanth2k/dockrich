import time
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from monisys.Managers.Systeminfo import SystemInfo

class SystemInfoCLI:
    def __init__(self):
        self.cpu_info = SystemInfo('cpu_info')
        self.kernel_info = SystemInfo('kernel_info')
        self.console = Console()

    def get_cpuinfo(self):
        address_width = self.cpu_info.get_values_by_key('address_width')
        cpu_status = self.cpu_info.get_values_by_key('cpu_status')
        current_clock_speed = self.cpu_info.get_values_by_key('current_clock_speed')
        device_id = self.cpu_info.get_values_by_key('device_id')
        logical_processors = self.cpu_info.get_values_by_key('logical_processors')
        manufacturer = self.cpu_info.get_values_by_key('manufacturer')
        max_clock_speed = self.cpu_info.get_values_by_key('max_clock_speed')
        model = self.cpu_info.get_values_by_key('model')
        number_of_cores = self.cpu_info.get_values_by_key('number_of_cores')
        processor_type = self.cpu_info.get_values_by_key('processor_type')
        socket_designation = self.cpu_info.get_values_by_key('socket_designation')

        return address_width,cpu_status,current_clock_speed,device_id,logical_processors,manufacturer,max_clock_speed,model,number_of_cores,processor_type,socket_designation
    def get_kernel_info(self):
        arguments = self.kernel_info.get_values_by_key('arguments')
        device = self.kernel_info.get_values_by_key('device')
        path = self.kernel_info.get_values_by_key('path')
        version = self.kernel_info.get_values_by_key('version')

        return arguments,device,path,version
    def display_uptime(self):
        try:
            cpu_info = self.get_cpuinfo()
            cpu_info_str = (
                f"Current Clock Speed: {cpu_info[2]}\n"
                f"Device id : {cpu_info[3]}\n"
                f"Number of cores: {cpu_info[9]}\n"
                f"Model: {cpu_info[7]}\n"
                f"Manufacturer: {cpu_info[5]}"
            )
            panel = Panel(cpu_info_str, title="CPU INFO", expand=False)
            console = Console()
            console.print(panel)
        except KeyboardInterrupt:
            print("[*] Closed")
    def display_kernel_info(self):
        try:
            kernel_info = self.get_kernel_info()
            kernel_info_string = (
                f"Arguments : {kernel_info[0]}\n"
                f"Device : {kernel_info[1]}\n"
                f"Path : {kernel_info[2]}\n"
                f"Version : {kernel_info[3]}"
            )
            panel = Panel(kernel_info_string,title="Kernal Info",expand=False)
            console = Console()
            console.print(panel)
        except KeyboardInterrupt:
            print("[*] Closed")