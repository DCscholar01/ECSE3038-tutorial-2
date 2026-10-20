readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]

def list_devices(readings):
    for device in readings:
        print(f"Device: {device['name']}, Temperature: {device['temp']}")

list_devices(readings)

def average_temp(readings):
    total = sum(device['temp'] for device in readings)
    return total / len(readings)

print(f"Average Temperature: {average_temp(readings)}")

def hottest(readings):
    return max(readings, key=lambda device: device['temp'])

print(f"Hottest Device: {hottest(readings)['name']}, Temperature: {hottest(readings)['temp']}")

def to_status(device):
    status = "online" if device['online'] else "offline"
    return {"name": device['name'], "status": status, "temperature": device['temp']}

# Example usage:
print(to_status(readings[3]))

def by_room(devices):
    room_dict = {}
    for device in devices:
        room = device['room']
        if room not in room_dict:
            room_dict[room] = []
        room_dict[room].append(device['name'])
    return room_dict

print(by_room(readings))