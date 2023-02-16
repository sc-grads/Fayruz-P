def remove_from_list(my_list, item):
    """
    Function that removes an item from a list.
    """
    while (item in my_list):  # check if the element belongs to the list
        my_list.remove(item)  # remove THE FIRST occurrence of the element


list1 = [1, 2, 1, 1, 1, 1, 3]

# Calling the function and remove 1 from the list
remove_from_list(list1, 1)

print(list1)  # => [2, 3]