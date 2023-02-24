# LIST METHODS
#
# l1 = list()
# l1.print(dir(l1))
# help(l1.append)

# Adding to the list: append(), extend(), insert()
l1 = [1, 2.2, 'abc']
# 1. list.append()
l1.append(5)
# l1.append([6,7]) # ERROR
l1.append([6,7])
print(l1)

# 2. list.extend()
l1.extend(['x','y'])
print(l1)

# 3. list.insert()
years = [2020, 2022, 2023]
years.insert(1, 2021)
years.insert(len(years),2024)
print(years)
years.insert(-1, 2025) # inserts on the second to last position
print(years)

# 4. list.clear()
years.clear()
print(years)

# 5. list.pop()
l2 = [10, 20, 30, 40]
x = l2.pop()
print(x)
print(l2)

y = l2.pop(1)
print(y, l2)
#  l2.pop(100) # ERROR

# 6. list.remove()
l3 = [10, 20, 10, 40, 20, 10, 20, 20, 'z']
l3.remove(x)
print(l3)
while 20 in l3:
    l3.remove(20)
print(l3)

# LIST METHODS - PART 2
print('#' * 20 + 'LIST METHODS - PART 2' + '#' * 20)
# 7. list.index()
names = ['john', 'dan', 'tom''john','bill']
i = names.index('dan', 1 , 3)
print(f'dan is index{i}')
print(names.index('john'))

# 8. list.count()
letter = list('sdvfhewfvhwvfhweajfdbvjdfbvj')
n = letter.count('a')
print(n)
print('p' in letter)

# 9. list.reverse()
l1 = [1, 3, 'abc', 10, 'x']
l1.reverse()
print(f'li:{l1}')

# 10. list.sort() and sorted(list)
ages = [10, 8, 23, 40, 35]
la = sorted(ages)
print(la, ages)

n = ages.sort()
print(n)
print(ages)
ages.sort(reverse=True)

l1 = [1, 3, '4']
# l1.sort() #ERROR

# 11. max() and min()
l2 = [-9, 10, 5, 100, 66]
print(f'max:{max(l2)}')
print(f'min:{min(l2)}')
print(f'sum:{sum(l2)}')