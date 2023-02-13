# For, continue and pass Statements

for letter in 'Go Python gooo!':
    if letter == 'o':
        continue
    print(letter, end='')

for n in range(10):
    if n % 2 == 0:
        print(f'Found and even number: {n}')
        continue
    print(f'Found an odd number: {n}')

for _ in range(100):
    pass

