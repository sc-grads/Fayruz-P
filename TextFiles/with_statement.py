with open('configuration.txt') as file:
    content = file.read()
    print(content)

print(file.closed) # True
#  file.read() => #ERROR: file closed
