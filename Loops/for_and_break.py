# For, else and break statements

for number in range(10):
    print(number)
    if number == 5:
        break
exit()
print('Outside for')

for letter in 'Python':
    if letter == 'o':
        print('letter is o and I\'m breaking out of the loop ...')
        break
    print(letter)

for n in range(0, 20):
    if n % 13 == 0:
        print('The is a number divisible by 13. Breaking out')
        break
else: # belongs to for
    print('No num div by 13.')

