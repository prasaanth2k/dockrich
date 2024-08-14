### Monisys - Moiniter entore os things

### Help message 
```bash
monisys -h or  --help
```
![helpmessage](https://github.com/user-attachments/assets/94eec1ca-49ed-4fdd-bd73-01c7959152a9)


```python3

import time
from monisys.Managers.Systeminfo import SystemInfo
system_info = SystemInfo('cpu_info')

cpuinfos = system_info.get_all_data()
print(cpuinfos)

```