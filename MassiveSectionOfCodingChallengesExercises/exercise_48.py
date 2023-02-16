def counter(my_str):
    vowels = 'aeiou'
    no_of_vowels = 0

    # letter case doesn't matter
    my_str = my_str.lower()  # make a lowercase copy of my_str

    for char in vowels:
        no_of_vowels += my_str.count(char)

    no_of_consonants = len(my_str) - no_of_vowels

    return (no_of_vowels, no_of_consonants)


print(counter('Python'))  # => (1, 5)
print(counter('BeautifUl'))  # => (5, 4)

