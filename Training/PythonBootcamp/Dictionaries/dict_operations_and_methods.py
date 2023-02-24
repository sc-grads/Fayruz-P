person = {'name': 'John' , 'age' : 30, 'location':'USA'}

friend = person
person['name'] = 'Peter'
print(friend)

neighbor = person.copy()
person['location'] = 'Europe'
print(neighbor, person)

countries = {'ro': 'Romania', 'us': 'USA', 'de': 'Germany'}
countries.update({'hu': 'Hungary', 'fr': 'France'})
print(countries)



# dict.key()
k = person.keys()
print(k)
print(type(k))
my_keys = list(k)
print(my_keys)

# dict.value()
print(person.values())
print(list(person.values()))

# dict.items()
print(person.items())

print('name' in person)
print(10 in person.keys())

print('USA' in person.values())

print(('age', 30) in person.items())

d1 = {10: 'a', 20: 'b', 30: 'c'}
v = d1.values()
d1[10] = 'X'
print(v)

d1 = {10: 'a', 20: 'b'}
d2 = {20: 'c', 30: 'c'}
k1 = d1.keys()
k2 = d2.keys()
print(k1, k2)

print(k1 & k2)
print(k | k2)

for k in person:
    print(f'key is  {k}')

for k in person.keys():
    print(f'key is {k} and value is {person[k]}')

for k,v in person.items():
    print(f'key is {k} and value is {v}')
