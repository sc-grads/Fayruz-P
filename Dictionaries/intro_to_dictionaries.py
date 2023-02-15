person = {'name': 'John', 'age': 30, (1, 2, 3): 100, 'age': 30}
print(type(person))
print(person)
d1 = dict()
# d2 = {}

print(len(person))

person['name'] = 'Dan'
print(person)

person['location'] = 'Berlin'
print(person)
a = person['age']
print(a)

value = person.get('city', 'Key does not exist')
print(value)

name = person.pop('name')
print(name,person)

print(person.popitem())

del person['age']
print(person)

germany = {
    'cities': ['Hamburg', 'Berlin', 'Munich'],
    'info': {'population' : 83_000_000, 'people': ['Einstein','Bach','Gauss']}
}
print(germany['cities'][1])
print(germany['info']['people'][0])
