# f = open('configuration.txt')
# content = f.read()
# print(content)
#
#
# content = f.read()
# print(content)
#
# print(f.tell())
# f.seek(2)
# content = f.read(3)
# print(content)
#
# f.seek(0)
# content = f.read(3)
# print(content)
#
f = open('configuration.txt')
print(f.read())
# do stuff

print('# ' * 50)
f.seek(0)
print(f.read())
