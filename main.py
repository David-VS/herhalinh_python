from devicemanager import DeviceManager
from device import Device

device1 = Device("Lamp 1", False)
device2 = Device("Lamp 2", False)
device3 = Device("Philips hue", True)
device4 = Device("Nest", False)

manager = DeviceManager()
manager.add_device(1, device1)
manager.add_device(2, device2)
manager.add_device(3, device3)
manager.add_device(4, device4)

manager.switch_everything_off()

for id, device in manager.device_dict.items():
    print(id)
    print(device)

