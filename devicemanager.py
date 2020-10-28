from device import Device

class DeviceManager:
    #composition, gebruik klassen binnen andere klasse
    device_dict = {}

    def __init__(self) :
        pass

    def add_device(self, id, device):
        self.device_dict[id] = device

    def remove_device(self, id):
        self.device_dict.pop(id)
        #alternatief
        #del self.device_dict[id]

    def switch_everything_on(self):
        for id in self.device_dict:
            device = self.device_dict[id]
            device.switch_on()

    def switch_everything_off(self):
        for id in self.device_dict:
            device = self.device_dict[id]
            device.switch_off()

    def toggle_everything(self):
        for id in self.device_dict:
            device = self.device_dict[id]
            if device.is_on:
                device.switch_off()
            else:
                device.switch_on()

