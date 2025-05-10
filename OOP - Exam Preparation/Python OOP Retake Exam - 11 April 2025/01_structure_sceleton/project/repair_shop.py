class RepairShop:
    def __init__(self, name: str, device_types: tuple):
        self.name = name
        self.device_types = device_types
        self.pending_devices: list = []
        self.repaired_devices: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Invalid repair shop name!")
        self.__name = value

    @property
    def device_types(self):
        return self.__device_types

    @device_types.setter
    def device_types(self, value):
        if not value:
            raise ValueError("No device types provided!")
        self.__device_types = value

    def repair(self):
        count_of_repaired = 0
        for device in self.pending_devices[:]:
            device.repair()
            self.repaired_devices.append(device)
            self.pending_devices.remove(device)
            count_of_repaired += 1
        return f"Repaired {count_of_repaired} device/s."

    def status(self):
        return (f"{self.name} has {len(self.pending_devices)} devices pending for repair "
                f"and {len(self.repaired_devices)} devices repaired.")
