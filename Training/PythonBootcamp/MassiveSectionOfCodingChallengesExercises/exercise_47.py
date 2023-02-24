def vowel_count(my_str):
    """
    This function counts the number of vowels in a string
    """
    vowels = 'aeiou'
    my_str = my_str.lower()  # ignoring the case (we consider only lower-case letters)

    # Dictionary that stores the result.
    result = dict()

    for char in my_str:
        if char in vowels:
            if char in result.keys():
                result[char] += 1
            else:
                result[char] = 1

    return result


r = vowel_count('Awesome')
print(r)  # => {'a': 1, 'e': 2, 'o': 1}

r = vowel_count('Wow! Python is great!')
print(r)  # => {'o': 2, 'i': 1, 'e': 1, 'a': 1}