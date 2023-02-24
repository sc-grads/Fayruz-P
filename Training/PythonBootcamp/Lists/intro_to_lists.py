# Python Lists

l1 = [1, 2.5, 'python', True, ['abc', 'xyz'],(10,20,30)]
print(len(l1))
l2 = []
l3 = list()
print(l1[0])
x = l1[-1]
print(x)

l4 = list('abc')
print(l4)
print(id(l4))
l4[0] = 'X'
l4.append(100)
print(l4)
