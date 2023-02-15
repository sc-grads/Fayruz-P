set1 = {1, 2, 3}
set2 = {2, 3, 1}
print(set1 == set2)
print(set1 is set2)

# SET METHODS
# 1. set.add()
s1 = {1, 2, 3}
s1.add('a')
s1.add(4.5)
print(s1)
s1.add(1) # does nothing

# 2. set.remove(item)
s1.remove(3)
print(s1)
# s1.remove(3) # ERROR

# 3.set.discard(item)
s1.discard('a')
s1.discard('x')

# 4. set.pop()
x = s1.pop()
print(x, s1)

s2 = set('abc')
s3 = s2
s3.add('x')
print(s2)

# 5. set.clear()
s3.clear()
print(f's2:{s2}, s3: {s3}')

# 6. set.copy()
s4 = s1.copy()
s4.add('z')
print(f's4:{s4}, s1: {s1}')