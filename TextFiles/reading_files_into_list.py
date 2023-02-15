# 1. f.read().splitlines()
with open('confiuration.txt')as f:
    content = f.read().splitlines()
    print(content)
print('#' * 50)

# 2. f.readlines()
with open('configuration.txt') as f:
    content = f.readlines()
    print(content)

with open('configuration.txt') as f:
    print(f.readline(), end='')

# 3. list(f)
with open('configuration.txt') as f:
    content = list(f)
    print(content)

# iterate over a file
with open('configuration.txt') as f:
    for line in f:
        print(line, end='')
