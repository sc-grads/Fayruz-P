alphabet = dict()
with open('phonetic_alphabet.csv') as f:
    content = f.read().splitlines()
    # print(content)
    for item in content[1:]:
        letter, word = item.split(',')
        alphabet[letter] = word
    print(alphabet)

my_str = 'abcdef'.upper()
print(my_str, end=' =>')
for char in my_str:
    print(alphabet[char], end='   ')
    