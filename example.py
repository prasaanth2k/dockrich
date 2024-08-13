import time
from monisys.Managers.Systeminfo import SystemInfo
kernel_info = SystemInfo('uptime')

names = kernel_info.get_values_by_key('hours')
print(names)
