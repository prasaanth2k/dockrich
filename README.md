### Monisys - Moiniter entore os things

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