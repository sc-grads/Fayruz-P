# Debugging your code

print('Hello Python!')
x = 101
y = x // 2

for n in [1, 2, 3, 4, 5, 6, 7]:
    nn = n ** 2
    if nn % 2 == 0:
        print(f'{nn} is even')
    else:
        print(f'{nn} is odd')