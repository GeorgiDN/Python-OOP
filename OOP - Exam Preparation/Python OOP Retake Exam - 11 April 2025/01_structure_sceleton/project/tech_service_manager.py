from project.devices.laptop import Laptop
from project.devices.smartphone import Smartphone
from project.devices.smartwatch import Smartwatch
from project.repair_shop import RepairShop


class TechServiceManager:
    VALID_DEVICES = {"Laptop": Laptop, "Smartphone": Smartphone, "Smartwatch": Smartwatch}

    def __init__(self):
        self.devices: list = []
        self.repair_shops: list = []

    def add_device(self, device_type: str, serial_number: str, durability: int, is_functional: bool):
        if device_type not in self.VALID_DEVICES:
            raise ValueError("Invalid device type!")

        new_device = self.VALID_DEVICES[device_type](serial_number, durability, is_functional)
        new_device.check_functionality()
        self.devices.append(new_device)
        return f"{device_type} is successfully added."

    def add_repair_shop(self, name: str, device_types: tuple):
        if not any(d_type in ("Laptop", "Smartphone", "Smartwatch") for d_type in device_types):
            raise ValueError("No valid device type!")

        new_shop = RepairShop(name, device_types)
        self.repair_shops.append(new_shop)
        return f"{name} is successfully added as a repair shop."

    def send_for_repair(self, repair_shop_name: str, device_type: str):
        shop = next((sh for sh in self.repair_shops if sh.name == repair_shop_name), None)
        if not shop or device_type not in shop.device_types:
            return "The shop cannot repair this device type."

        device = next((d for d in self.devices if d.device_type == device_type and not d.is_functional), None)
        if not device:
            return f"There is no {device_type} that needs repair."

        self.devices.remove(device)
        shop.pending_devices.append(device)
        return f"{device.serial_number} was sent for repair to {repair_shop_name}."

    def process_repairs(self, repair_shop):
        return repair_shop.repair()

    def receive_repaired_devices(self, repair_shop):
        count_repaired_devices = len(repair_shop.repaired_devices)
        self.devices.extend(repair_shop.repaired_devices)
        repair_shop.repaired_devices.clear()
        return f"Received {count_repaired_devices} repaired devices."

    def tech_service_status(self):
        result = ["***Tech Service***"]
        functional_count = sum(d.is_functional for d in self.devices)
        not_functional_count = len(self.devices) - functional_count

        sorted_repaired_shops = sorted(self.repair_shops, key=lambda sh: sh.name)
        repair_shops_status = '\n'.join(
            f"@{shop.status()}" for shop in sorted_repaired_shops)

        result.append(f"Total number of functional devices: {functional_count}")
        result.append(f"Total number of malfunctioning devices: {not_functional_count}")
        result.append(f"Repair shops count: {len(self.repair_shops)}")
        result.append(f"{repair_shops_status}")

        return "\n".join(result)


# # TEST code
# Create the service manager
# manager = TechServiceManager()
#
# # Add devices
# print(manager.add_device("Laptop", "LPT1234A", 40, True))
# print(manager.add_device("Laptop", "LPT5678B", 1, True))
# print(manager.add_device("Laptop", "LZT5678B", 2, True))
# print(manager.add_device("Smartphone", "SPH0001X", 10, False))
# print(manager.add_device("Smartphone", "SPH0002Y", 80, True))
# print(manager.add_device("Smartphone", "SYH0002Y", 1, True))
# print(manager.add_device("Smartwatch", "SZT3009Z", 5, False))
# print(manager.add_device("Smartwatch", "SWT3009Z", 5, False))
# print()
#
# # Add repair shops
# print(manager.add_repair_shop("BFixIt Center", ("Desktop", "Laptop", "Smartphone", "Smartwatch")))
# print(manager.add_repair_shop("AQuickFix", ("HomeAI", "Smartwatch")))
# print()
#
# # Send devices for repair
# print(manager.send_for_repair("BFixIt Center", "Laptop"))
# print(manager.send_for_repair("BFixIt Center", "Smartphone"))
# print(manager.send_for_repair("BFixIt Center", "Smartwatch"))
# print(manager.send_for_repair("BFixIt Center", "Laptop"))
# print(manager.send_for_repair("AQuickFix", "Smartphone"))
# print(manager.send_for_repair("AQuickFix", "Smartwatch"))
# print()
#
# # Process repairs at first shop
# print(manager.process_repairs(manager.repair_shops[0]))
# print(manager.process_repairs(manager.repair_shops[0]))
# print()
#
# # Display current service status
# print(manager.tech_service_status())
# print()
#
# # Receive repaired devices
# print(manager.receive_repaired_devices(manager.repair_shops[0]))
# print(manager.receive_repaired_devices(manager.repair_shops[1]))
# print()
#
# # Display final service status
# print(manager.tech_service_status())


"""
Laptop is successfully added.
Laptop is successfully added.
Laptop is successfully added.
Smartphone is successfully added.
Smartphone is successfully added.
Smartphone is successfully added.
Smartwatch is successfully added.
Smartwatch is successfully added.

BFixIt Center is successfully added as a repair shop.
AQuickFix is successfully added as a repair shop.

LPT5678B was sent for repair to BFixIt Center.
SPH0001X was sent for repair to BFixIt Center.
SZT3009Z was sent for repair to BFixIt Center.
There is no Laptop that needs repair.
The shop cannot repair this device type.
SWT3009Z was sent for repair to AQuickFix.

Repaired 3 device/s.
Repaired 0 device/s.

***Tech Service***
Total number of functional devices: 3
Total number of malfunctioning devices: 1
Repair shops count: 2
@AQuickFix has 1 devices pending for repair and 0 devices repaired.
@BFixIt Center has 0 devices pending for repair and 3 devices repaired.

Received 3 repaired devices.
Received 0 repaired devices.

***Tech Service***
Total number of functional devices: 6
Total number of malfunctioning devices: 1
Repair shops count: 2
@AQuickFix has 1 devices pending for repair and 0 devices repaired.
@BFixIt Center has 0 devices pending for repair and 0 devices repaired.
"""
