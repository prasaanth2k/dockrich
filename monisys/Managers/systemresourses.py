import subprocess
import json

class Cpuinforesponse:
    def __init__(self, data=None):
        if data is None:
            # Fetch CPU info automatically if no data is provided
            data = self.fetch_cpu_info()

        self.address_width = data.get("address_width")
        self.cpu_status = data.get("cpu_status")
        self.current_clock_speed = data.get("current_clock_speed")
        self.device_id = data.get("device_id")
        self.logical_processors = data.get("logical_processors")
        self.manufacturer = data.get("manufacturer")
        self.max_clock_speed = data.get("max_clock_speed")
        self.model = data.get("model")
        self.number_of_cores = data.get("number_of_cores")
        self.processor_type = data.get("processor_type")
        self.socket_designation = data.get("socket_designation")

    def fetch_cpu_info(self):
        try:
            cpuinfo = ["osqueryi", "--json", "SELECT * FROM cpu_info;"]
            output = subprocess.run(cpuinfo, capture_output=True, check=True, text=True)
            result = json.loads(output.stdout)
            return result[0] if result else {}  # Return the first CPU's data if available
        except subprocess.CalledProcessError as e:
            print(f"Error running command {e.cmd}: {e.output}")
            return {}

    def __repr__(self) -> str:
        return f"<Cpuinforesponse {self.__dict__}>"

