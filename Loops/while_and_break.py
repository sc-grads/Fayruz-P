# While And Break

while True:
    guess = int(input('Enter uour lucky number [1-10]:'))
    if guess == 7:
        print('You won!')
        break
    print(f'{guess} was not a lucky number!')
