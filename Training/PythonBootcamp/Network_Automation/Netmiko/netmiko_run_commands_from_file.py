from netmiko import ConnectHandler
cisco_device = {
    'device_type': 'cisco_ios',
    'host': '10.1.1.10',
    'username': 'u1',
    'password': 'cisco',
    'port': 22,
    'secret': 'cisco',
    'verbose': True
}

connection = ConnectHandler(**cisco_device)
print('Entering the enable mode....')
connection.enable()

print('Sending commands from file ....')
connection.send_config_from_file('ospf.txt')

print('Closing connection')
connection.disconnect()