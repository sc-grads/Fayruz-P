s1 = {1, 2, 3, 'a', 'b', 4, 1, 2, 'a', 3, 10}
print(s1)
# print(s1[0]) # EEROR

# SETS ARE MUTABLE
s1.add((10,20))
print(s1)

s1.remove('a')
print(s1)

s2 = set()
s3 = {}
print(type(s3))

# str => set
s4 = set('Hellooooo!!!')
print(s4)

# tuple => set
s5 = set((1, 2, 3, 4, 4, 'abc'))
print(s5)

# list => set
l2 = [10, 20, 30, 40]
print(set(l2))

for item in s4:
    print(item)

print('x' in s4)

