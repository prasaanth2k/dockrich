import subprocess
import json
from typing import List


class ACPIResponse:
    def __init__(self, data: dict):
        self.md5 = data.get("md5")
        self.name = data.get("name")
        self.size = data.get("size")

    def __repr__(self) -> str:
        return f"<ACPIResponse {self.__dict__}>"


class ApparmorprofilesResponse:
    def __init__(self, data: dict):
        self.attach = data.get("attach")
        self.mode = data.get("mode")
        self.name = data.get("name")
        self.path = data.get("path")
        self.sha1 = data.get("sha1")

    def __repr__(self) -> str:
        return f"<ApparmorResponse {self.__dict__}>"


class EssentialsManager:

    def acpi_tables(self) -> List[ACPIResponse]:
        """
        ACPI is advanced configuration power interface it is basicly stored in system level memory
        and it will manages to configure and computer harware components
        """
        try:
            acpi_tables = ["osqueryi", "--json", "SELECT * FROM acpi_tables;"]
            output = subprocess.run(acpi_tables, capture_output=True, check=True)
            result = json.loads(output.stdout)
            responses = [ACPIResponse(acpi_tables) for acpi_tables in result]
            return responses
        except subprocess.CalledProcessError as e:
            print(f"Error running command {e.cmd}: {e.output}")
            return []

    def apparmor_profiles(self) -> List[ApparmorprofilesResponse]:
        """
        Apparmor profiles it is an basicly an type of linux harderining and main text files it will
        run on linux operating system
        """
        try:
            apparmor_profiles = ["osqueryi","--json","SELECT * FROM apparmor_profiles;",]
            output = subprocess.run(apparmor_profiles, capture_output=True, check=True)
            result = json.loads(output.stdout)
            responses = [ApparmorprofilesResponse(apparmor_profiles) for apparmor_profiles in result]
            return responses
        except subprocess.CalledProcessError as e:
            print(e.cmd)
