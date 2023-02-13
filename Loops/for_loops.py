# For Loops
# for letter in 'Python':
#     print(letter)
#     print('bye')
#     print('####')

my_str = input("Enter something:")
vowels = 'aeiou'
for item in my_str:
    if item in vowels:
        print(item, end= ' ')
