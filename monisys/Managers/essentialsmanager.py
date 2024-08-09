import subprocess
import json
from typing import List


class ACPIResponse:
    def __init__(self, data=None):
        if data is None:
            data = self.fetch_acpi_tables()
        self.md5 = data.get("md5")
        self.name = data.get("name")
        self.size = data.get("size")

    def fetch_acpi_tables(self):
        try:
            acpi_tables = ["osqueryi", "--json", "SELECT * FROM acpi_tables;"]
            output = subprocess.run(acpi_tables, capture_output=True, check=True, text=True)
            result = json.loads(output.stdout)
            return result[0] if result else {}
        except subprocess.CalledProcessError as e:
            print(f"Error running command {e.cmd}: {e.output}")
            return {}

    def __repr__(self) -> str:
        return f"<ACPIResponse {self.__dict__}>"


class ApparmorprofilesResponse:
    def __init__(self, data=None):
        if data is None:
            data = self.fetch_apparmor_profiles()
        self.attach = data.get("attach")
        self.mode = data.get("mode")
        self.name = data.get("name")
        self.path = data.get("path")
        self.sha1 = data.get("sha1")

    def fetch_apparmor_profiles(self):
        try:
            apparmor_profiles = ["osqueryi", "--json", "SELECT * FROM apparmor_profiles;"]
            output = subprocess.run(apparmor_profiles, capture_output=True, check=True, text=True)
            result = json.loads(output.stdout)
            return result[0] if result else {}
        except subprocess.CalledProcessError as e:
            print(f"Error running command {e.cmd}: {e.output}")
            return {}

    def __repr__(self) -> str:
        return f"<ApparmorprofilesResponse {self.__dict__}>"


class AuthorizedkeysResponse:
    def __init__(self, data=None):
        if data is None:
            data = self.fetch_authorized_keys()
        self.algorithm = data.get("algorithm")
        self.comment = data.get("comment")
        self.key = data.get("key")
        self.key_file = data.get("key_file")
        self.options = data.get("options")
        self.uid = data.get("uid")

    def fetch_authorized_keys(self):
        try:
            authorized_keys = ["osqueryi", "--json", "SELECT * FROM authorized_keys;"]
            output = subprocess.run(authorized_keys, capture_output=True, check=True, text=True)
            result = json.loads(output.stdout)
            return result[0] if result else {}
        except subprocess.CalledProcessError as e:
            print(f"Error running command {e.cmd}: {e.output}")
            return {}

    def __repr__(self) -> str:
        return f"<AuthorizedkeysResponse {self.__dict__}>"


class EssentialsManager:

    def acpi_tables(self) -> List[ACPIResponse]:
        """
        ACPI is advanced configuration power interface; it is basically stored in system-level memory
        and it will manage to configure and computer hardware components.
        """
        try:
            acpi_tables = ["osqueryi", "--json", "SELECT * FROM acpi_tables;"]
            output = subprocess.run(acpi_tables, capture_output=True, check=True, text=True)
            result = json.loads(output.stdout)
            responses = [ACPIResponse(acpi_table) for acpi_table in result]
            return responses
        except subprocess.CalledProcessError as e:
            print(f"Error running command {e.cmd}: {e.output}")
            return []

    def apparmor_profiles(self) -> List[ApparmorprofilesResponse]:
        """
        AppArmor profiles are a type of Linux hardening, primarily used to confine the access of applications
        to certain files and capabilities on the Linux operating system.
        """
        try:
            apparmor_profiles = ["osqueryi", "--json", "SELECT * FROM apparmor_profiles;"]
            output = subprocess.run(apparmor_profiles, capture_output=True, check=True, text=True)
            result = json.loads(output.stdout)
            responses = [ApparmorprofilesResponse(apparmor_profile) for apparmor_profile in result]
            return responses
        except subprocess.CalledProcessError as e:
            print(f"Error running command {e.cmd}: {e.output}")
            return []

    def authorized_keys(self) -> List[AuthorizedkeysResponse]:
        """
        Fetch the list of authorized keys used for SSH access.
        """
        try:
            authorized_keys = ["osqueryi", "--json", "SELECT * FROM authorized_keys;"]
            output = subprocess.run(authorized_keys, capture_output=True, check=True, text=True)
            result = json.loads(output.stdout)
            responses = [AuthorizedkeysResponse(authorized_key) for authorized_key in result]
            return responses
        except subprocess.CalledProcessError as e:
            print(f"Error running command {e.cmd}: {e.output}")
            return []