# Ranges

r = range(2, 10, 3)
print(type(r))
print(list(r))

print(list(range(0, 11, 2)))
print(list(range(0, 40, 7)))
s = sum(range(0, 1001))
print(s)

#Summary
# 1. range(stop)
print(list(range(10))) # range(0, 10, 1)

# 2. range(start, stop)
print(list(range(3, 9))) # range(3, 9, 1)

# 3. range(start,stop step)
print(list(range(5, 100, 13)))

print(list(range(-20, 10, 4)))

#exercise
# Using the built-in range() function, create the following lists of numbers:
# list1 = [-10, -7, -4, ... , 92, 95, 98]
# list2 = [99, 97, 95, ..., 1, -1, -3]

## YOUR CODE STARTS HERE

list1 = list(range(-10, 99, 3))
print(list1)
list2 = list(range(99, -4 , -2))
print(list2)
