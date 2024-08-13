import time
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from monisys.Managers.Systeminfo import SystemInfo

class SystemInfoCLI:
    def __init__(self):
        self.kernel_info = SystemInfo('uptime')
        self.console = Console()

    def get_uptime(self):
        days = self.kernel_info.get_values_by_key('days')
        hours = self.kernel_info.get_values_by_key('hours')
        minutes = self.kernel_info.get_values_by_key('minutes')
        seconds = self.kernel_info.get_values_by_key('seconds')
        total_seconds = self.kernel_info.get_values_by_key('total_seconds')

        return days, hours, minutes, seconds, total_seconds

    def display_uptime(self):
        try:
            with Live(console=self.console, screen=False) as live:
                while True:
                    uptime = self.get_uptime()
                    uptime_str = (
                        f"Days: {uptime[0]}\n"
                        f"Hours: {uptime[1]}\n"
                        f"Minutes: {uptime[2]}\n"
                        f"Seconds: {uptime[3]}\n"
                        f"Total Seconds: {uptime[4]}"
                    )
                    panel = Panel(uptime_str, title="System Uptime", expand=False)
                    live.update(panel)
                    time.sleep(1)
        except KeyboardInterrupt:
            pass

