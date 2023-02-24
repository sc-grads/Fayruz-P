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

# commands = ['int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'exit', 'username netmiko secret cisco']
# cmd = 'ipssh version 2;access-list 1 permit any;ip domain-name network automation.io'
cmd = '''ip ssh version 2
access-list 1 permit any
ip domain-name net-auto.io'''


output = connection.send_config_set(cmd.split(';'))
print(output)
print(connection.find_prompt())

connection.send_command('write memory')

print('Closing connection')
connection.disconnect()