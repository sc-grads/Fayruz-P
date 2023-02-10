# Challenge 1
#  Write a Python script that extracts the MAC address (b4:6d:83:77:85:f3) from the string.

my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'
address = my_str[len(my_str)-17:]
print(address)

# Challenge 2

message = 'It displayed: "You\'ve got an error!"'
print(message)

print('\\n means a new line.')

print('\\ is known as the escape character.')

# Challenge #3

# Write a Python script that converts foot [ft] to centimeter [cm]. 1 ft = 30.48 cm
# The user will be prompted to enter the value in ft.
# Display the value in cm with 2 decimals, formatted using an f-string.

foot = input('Enter value in ft:')
cm = float(foot) * 30.48
print(f'{foot} foot = {cm:.2f} cm')

# Challenge #4

# Write a Python script that tests if a string is a palindrome.

p = 'madam'
print(f'Is p palindrome? => {p == p[::-1]}')

#  Challenge #5

# Change the solution of the previous challenge so that both the white spaces and the letter case are ignored when checking if the string is a palindrome.

name = 'My name is Fayruz'
name = name.replace(' ', '')
name = name.lower()
print(f'Is name a palindrome? => {name == name[::-1]}')

# Challenge #6
#
# Write a Python script to get a string made of the first and the last 2 chars from a given string entered by the user.
#
# Sample String: 'Hello!'
#
# Expected Result: 'Heo!'

this_str = input('Enter a word:')
new_str = this_str[:2] + this_str[-2:]
print(new_str)

# Challenge #7
#
# Write a Python program to get a string from a given string where all occurrences of its first character have been changed to '$', except the first character itself.
#
# Sample String: 'mama'
#
# Expected Result: 'ma$a'
a_str = 'mama'
new_str2 = a_str[1:].replace('m', '$')
print(a_str[0] + new_str2)

# Challenge #8
#
# Write a Python program to remove the nth index character from a nonempty string.

n = int(input('Enter the nth index char to remove:'))
my_str = input('Enter the string to change:')
first_part = my_str[0:n]
last_part = my_str[n+1:]
new_str = first_part + last_part
print(new_str)

# Challenge #9
#
# Write a Python script that removes the characters which have odd index values of a given string.

a_str = 'apples'
new_a_str = a_str[::2]
print(new_a_str)

# Challenge #10
#
# Write a Python script that prompts the user for the radius of a circle and calculates its area. Circle's area = pi * r ** 2 where pi = 3.1415
#
# Using an f-string display the area of the circle with 4 decimal places.

r = float(input('Enter radius of circle:'))
pi = 3.1415
circle_area = pi * r ** 2
print(f'The area of the circle with radius {r} is {circle_area:.4f}')

# Challenge #11
# #
# # Write a Python script that finds all occurrences of a substring in a given string by ignoring the letter case.
d = 'This is Python Bootcamp!'
k = 'Python'
e = d.lower()
f = d.count(k.lower())
print(f)

# Challenge #12
#
# Write a Python script that displays a number with a comma (,) as the thousands separator (US and UK format) and with a period(.) as the thousands separator (EU format).

n = 12384756982
n_comma = f'{n:,}'

print(n_comma)

print(n_comma.replace(',', '.'))