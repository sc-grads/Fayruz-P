# from netmiko import Netmiko
#
# connection = Netmiko(host='10.1.1.10', port = '22', username = 'u1',password = 'cisco', device_type='cisco_ios')

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
prompt = connection.find_prompt()
if '>' in prompt:

    connection.enable()

output = connection.send_command('sh run')
print(output)

if not connection.check_config_mode():
    connection.config_mode()

# print(connection.check_config_mode())
connection.send_command('username u3 secret cisco')


connection.exit_config_mode()

print('Closing connection')
connection.disconnect()
