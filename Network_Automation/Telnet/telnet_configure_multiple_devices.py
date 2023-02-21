import telnetlib
import time

router1 = {'host':'10.1.1.10', 'user': 'u1', 'password': 'cicso'}
router2 = {'host':'10.1.1.20', 'user': 'u1', 'password': 'cicso'}
router3 = {'host':'10.1.1.30', 'user': 'u1', 'password': 'cicso'}

routers = {router1,router2, router3}

for router in routers:
    print(f'Connecting to {router["host"]}')

    tn = telnetlib - telnetlib.Telnet(host=router['host'])

    tn.read_until(b'Username: ')
    tn.write(router['user'].encode()) + b'\n'

    tn.read_until(b'Password: ')
    tn.write(router['password'].encode() + b'\n')

    tn.write(b'terminal length 0\n')
    tn.write(b'show ip interface brief\n')
    tn.write(b'cisco')  # this is enable password
    tn.write(b'conf t\n')
    tn.write(b' ip route 0.0.0.0.0.0.0.0 e0/0 10.1.1.2\n')
    tn.write(b'end\n')
    tn.write(b'show in ip route\n')
    tn.write(b'exit\n')
    time.sleep(1)

    output = tn.read_all()
    print(type(output))
    output = output.decode
    print(output)
