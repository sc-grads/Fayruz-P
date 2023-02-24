import telnetlib
import time

host = '10.1.1.10'
port = '23'
user = 'u1'
password = 'cisco'

tn = telnetlib - telnetlib.Telnet(host=host, port=port)

tn.read_until(b'Username: ')
tn.write(user.encode()) + b'\n'

tn.read_until(b'Password: ')
tn.write(password.encode() + b'\n')


tn.write(b'terminal length 0\n')
tn.write(b'show ip interface brief\n')
tn.write(b'cisco') # this is enable password
tn.write(b'show run\n')
tn.write(b'exit\n')
time.sleep(1)

output = tn.read_all()
print(type(output))
output = output.decode
print(output)