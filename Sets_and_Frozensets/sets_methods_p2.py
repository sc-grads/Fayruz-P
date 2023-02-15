set1 = {1, 3, 5}
set2 = {5, 7, 9}

# 1. set.intersection()
set3 = set1.intersection(set2)
print(f'set3: {set3}')
set3 = set1 & set2
print(f'set3: {set3}')

# 2. set.difference()
set4 = set1.difference(set2)
print(f'set3: {set4}')
set4 = set1 & set2
print(f'set4: {set4}')

# 3. set.symmetric_difference()
set5 = set1.symmetric_difference(set2)
print(f'set5: {set5}')
set5 = set1 ^ set2
print(f'set5: {set5}')

# 4. set.union()
set6 = set1.union(set2)
print(f'set6:{set6}')

# 5. set.isdisjoint()
s1 = {1, 3, 5}
s2 = {5, 6, 7}
print(s1.isdisjoint(s2))
s3 = {8, 9}
print(s1.isdisjoint(s3))

# <, <=, >, >=
print({1, 3} < {1, 2, 3, 4})
