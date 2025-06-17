class Device:
    def __init__(self, deviceId, deviceName, latitude, longitude):
        self.deviceId = deviceId
        self.deviceName = deviceName
        self.latitude = latitude
        self.longitude = longitude
    def to_dict(self):
        return {
            'deviceId': self.deviceId,
            'deviceName': self.deviceName,
            'latitude': self.latitude,
            'longitude': self.longitude
        }