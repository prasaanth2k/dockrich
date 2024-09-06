### Monisys - Moiniter entore os things
![monisys](https://github.com/user-attachments/assets/db339f64-c42c-42d4-9414-62706b0a5820)


Install as sudo 
```bash
sudo pip install monisys
```
### Help message 
```bash
monisys -h or  --help
```
![helpmessage](/images/helpmessage.png)


```python3

import time
from monisys.Managers.Systeminfo import SystemInfo
system_info = SystemInfo('cpu_info')

cpuinfos = system_info.get_all_data()
print(cpuinfos)

```
