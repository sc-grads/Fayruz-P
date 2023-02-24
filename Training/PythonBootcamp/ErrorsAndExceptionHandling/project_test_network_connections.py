import subprocess


with open('hosts.txt') as f:
    ip_addresses = f.read().splitlines()
    # print(ip_addresses)
    for ip in ip_addresses:
        try:
            command = f'ping -n 1 {ip}'
            output = subprocess.check_output(command.split())
            print(output.decode())
        except Exception as e:
            print(f'Host{ip} is down!!! => {e}')
