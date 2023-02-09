# Converting Types

# 1 miles = 1.609 km
miles = float(input('Enter distance in miles:'))
# print(type(miles))
# miles = float(miles)
km = miles * 1.609
print('Distance in km:', km)

a = 10
b = 2.5
c = '8.2'

# int => float
a_float = float(a)
print('a:',type(a))
print('a_float:',type(a_float))

# float => float
b_int = int(b)
print('b_int:' , type(b_int))

# str => float
c_float = float(c)
print('c_float:', type(c_float))

#str => int
c_int = int(float(c))

# str = 's'
# a = 1
# a_str = str(a)
# above gives error because it tries to call the variable str instead of the type.

# Coding Exercise

a = '1.5'
b = '2'
#  Using Type Casting create a new variable called c that stores the result of a multiplied by b. c stores a float and will be 3.0.
c = float(a) * float(b)
print(c)
