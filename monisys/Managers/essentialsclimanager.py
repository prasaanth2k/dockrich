import subprocess
import json


class EssentialsManagercli:
    
    def acpi_tables(self):
        '''
        ACPI is advanced configuration power interface it is basicly stored in system level memory
        and it will manages to configure and computer harware components
        '''
        try:
            acpi_tables = ["osqueryi","--json","SELECT * FROM acpi_tables;"]
            output = subprocess.run(acpi_tables, capture_output=True, check=True)
            result = json.loads(output.stdout)
            return result
        except subprocess.CalledProcessError as e:
            print(e.cmd)
    def apparmor_profiles(self):
        '''
        Apparmor profiles it is an basicly an type of linux harderining and main text files it will 
        run on linux operating system
        '''
        try:
            apparmor_profiles = ["osqueryi","--json","SELECT * FROM apparmor_profiles;"]
            output = subprocess.run(apparmor_profiles,capture_output=True,check=True)
            result = json.loads(output.stdout)
            return result
        except subprocess.CalledProcessError as e:
            print(e.cmd)