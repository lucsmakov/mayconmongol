from models.device import Device
devices = []
id_device = 0
def id_generator():
    global id_device
    id_device += 1
    return id_device

def create_device(info):
    global devices
    for x in devices:
        if x.deviceId == info['deviceId']:
            return None, "the device id already exists"
    new_device = Device(id_generator(), info['deviceName'], info['longitude'], info['latitude'])
    devices.append(new_device)
    return new_device, None

def device_list():
    return [x.to_dict() for x in devices]

def chosen_device_list(id):
    for x in devices:
        if x.deviceId == id:
            return x, None
    return None, "device not found"

def update_device(id, new_info):
    erro, device_found = chosen_device_list(id)
    if erro:
        return None, erro
    for x in devices:
        if x.deviceName == new_info['deviceName'] and x.deviceId != id:
            return None, "the device name already exists"
    if device_found:
        device_found.deviceName = new_info['deviceName'] if 'deviceName' in new_info else device_found.deviceName
        return device_found, "device updated successfully"
    
def delete_device(id):
    global devices
    device = chosen_device_list(id)
    if device:
        devices.remove(device)
        return True
    