with open('devices.txt') as f:
    content = f.read().splitlines()
    devices = list()
    for line in content[1:]:
        devices.append(line.split())

    print(devices)

for device in devices:
    print(f'pinging {device[1]}')
