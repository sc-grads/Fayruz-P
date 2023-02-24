my_tuple = (1.4, 10, 'abc', True, (30, 40), 'x')
t1 = my_tuple + tuple('vy')
print(t1)

t2 = (1, 2, 'a') * 3
print(t2)
print(my_tuple[0:2])
print(my_tuple[:3])
print(my_tuple[2:])
print(my_tuple[::])
print(my_tuple[::2])
print(my_tuple[-1:0:-1])
movies = ('The Godfather', 'Nemo', 'The Matrix')
for movie in movies:
    print(f'We are watching{movie}')

print('The Matrix' in movies)
print('The Matrix' not in movies)