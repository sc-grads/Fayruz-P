# String Methods

# print(), len(), type(), sum(), max(), min(), round()

print(len('cbjsbf'))
print(dir(str))
help(str.replace)

s = 'Python'
new_s = s.upper()
print(s)
print(new_s)

print('proGRAMING'.lower())
s.capitalize()

# String Methods

my_str = 'I learn Pythong Programming'

#1. str.upper()
print(my_str.upper())

#2. str.lower()
print(my_str.lower())

#3. str.strip()
ip = '  192.168.0.1    '
ip = ip.strip()
print(ip)

value = '$$200$$$$'
print(value.strip('$'))

# 4. str.replace()
new_value = value.replace('$' , "&")
print(new_value)

# 5. str.count()
txt = 'I learn pythoN, pyThon is cool!'
n = txt.lower().count('python')
print(n)

print(txt.count('y'))

# 6. str.split()
my_list = txt.split()
print(my_list)

print('10.1.2.3'.split('.'))

# 7. str.join()
ip = '10.1.2.3'
ip_list = ip.split('.')
print(ip_list)

ip_str = '.'.join(ip_list)
print(ip_str)

ip_str = 'xxxx'.join(ip_list)
print(ip_str)

# 8. str.find()
my_str = 'I learn Python Programming.'
print(my_str.find('Python'))

# in
print('Python' in my_str)

# not in
print('Golang' in my_str)

# Exercise
language ='$Python$$'
message = 'I love Python!'

# YOUR CODE STARTS HERE:
language1 = language.strip('$')
language2 = language1.lower()
message1 = message.upper()
message2 = message.replace('Python', 'Java')
