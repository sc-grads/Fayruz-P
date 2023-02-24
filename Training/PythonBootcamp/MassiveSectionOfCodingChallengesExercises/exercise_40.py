my_str  = 'wlo1      Link encap:Ethernet  HWaddr b4:6d:83:77:85:f3'

# YOUR CODE STARTS HERE
my_list = my_str.split()

interface_mac = my_list[0] + '!' + my_list[-1]