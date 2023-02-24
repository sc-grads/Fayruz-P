import time

import paramiko

ssh_client = paramiko.SSHClient()
# print(type(ssh_client))

print('Connecting to 10.1.1.10')
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh_client.connect(hostname='10.1.1.10', port='22', username='u1', password='cisco',
#                    look_for_keys=False,allow_agent=False)

router = {'hostname': '10.1.1.10', 'port': '22', 'username': 'u1'}
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
print(ssh_client.get_transport().is_active())


shell = ssh_client.invoke_shell()
shell.send('terminal length 0\n')
shell.send('show version\n')
shell.send('show ip int brief\n')
time.sleep(1)

output = shell.recv(10000)
print(type(output))
output = output.decode('utf-8')
print(output)


if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()
