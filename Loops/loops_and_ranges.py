# Loops and Ranges

s = 0
for n in range(101):
    s += n
print(f'Sum: {s}')

for _ in range(10):
    print('Do something', _)

import random

names = ['Diana', 'Paul', 'Ana', 'Dan']
for _ in range(3):
    print(f'Choosing winner. Round {_} ...')
    winner = random.choice(names)
    names.remove(winner)
    print(winner)

