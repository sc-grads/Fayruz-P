def reverse(my_str):
    """
    This function returns a new string with all characters reversed.
    """
    return my_str[::-1]  # slicing with a step of -1


output = reverse('Beautiful')
print(output)  # => lufituaeB