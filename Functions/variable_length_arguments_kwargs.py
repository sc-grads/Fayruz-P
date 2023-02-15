def my_function(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(f'k is {k} and v is {v}')

def connect(ip, port, username, password):
    print(ip, port, username, password)


# my_function(name = 'John', age = 40, location = 'London')
# person = {'name': 'Andreas', 'age': 30, 'location': 'Berlin'}
# my_function(**person)