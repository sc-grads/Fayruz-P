#################################
## Running System (shell) commands
#################################


## Running system commands using os module
import os

## Running 'arp -a' command and getting the output
output = os.popen('arp -a').read()
print(output)  # => (192.168.0.1) at 90:5c:44:05:91:26 [ether] on wlo1

## Running 'ipconfig' command on Windows and getting the output
# output = os.popen('ipconfig').read()
# print(output)   # printing the output of ipconfig command

## It's not recommended to execute commands using os.system()
# os.system('whatever command')


## Running system commands using subprocess module
import subprocess

# subprocess.check_output() is used to run a command and capture the output
# subprocess.check_call() is used to run a command without capture the output

## The command and its options and arguments is a list
cmd = ['arp', '-a']
output = subprocess.check_output(cmd)  # running the command and getting the output
print(output.decode())  # output is of type bytes, decoding to string and print it out

cmd = ['ping', '-c 1', '8.8.8.8']  # Linux command
# cmd = ['ping', '-n 1', '8.8.8.8']     # Windows command
output = subprocess.check_output(cmd)  # Running the command and getting the output
print(output.decode())  # Decoding from bytes to string

# Output:
# --- 8.8.8.8 ping statistics ---
# 1 packets transmitted, 1 received, 0% packet loss, time 0ms
# rtt min/avg/max/mdev = 34.776/34.776/34.776/0.000 ms


## Spliting the command string to a list, executing it and decoding the output to a string
output = subprocess.check_output('ping -c 1 8.8.8.8'.split()).decode()
print(output)

# Output:
# --- 8.8.8.8 ping statistics ---
# 1 packets transmitted, 1 received, 0% packet loss, time 0ms
# rtt min/avg/max/mdev = 34.776/34.776/34.776/0.000 ms