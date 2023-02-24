with open('show_arp.txt', 'r', newline='') as f:
    # Reading file in list (each line is list element)
    contents = f.read().splitlines()

    # The argument newline='' is necessary only in Windows

    # Eliminating the first item from the list (files header)
    contents = contents[1:]

    # Empty list that stores tuples like (ip, mac)
    ip_mac = list()

    # Iterating over the list(file contents) line by line
    for line in contents:
        ip = line.split()[1]  ## Getting the IP
        mac = line.split()[3]  ## Getting the MAC

        # Adding the tuple to the ip_mac list
        ip_mac.append((ip, mac))

    print(ip_mac)