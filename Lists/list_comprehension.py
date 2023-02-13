# LIST COMPREHENSION
clicks = [10, 5, 15, 20]
doubled_list = list()
for c in clicks:
    doubled_list.append(c*2)
print(doubled_list)

# [expression for item in iterable]
doubled_numbers = [c*2 for c in clicks]
print(doubled_numbers)

name = 'Andrei'
l1 = [char for char in name]
print(l1)

l2 = [char * 3 for char in name]
print(l2)

friends = ['Andrei', 'Diana', 'Paul', 'Marry']
my_friends = [item.capitalize() for item in friends]
print(my_friends)

reversed_names = [item[::-1] for item in friends]
print(reversed_names)

nums = [1, 7, 8, 14, 21, 23, 50]
divisible_by_seven = [n for n in nums if n % 7 == 0]
print(divisible_by_seven)

nums_str = [str(n) for n in nums]
print(nums_str)
print('-'.join(nums_str))

friends = ['JoHn', 'dan', 'Mary']
neighbors = ['Tim', 'Steve', 'Dan','John']
friends_and_neighbors = [name for name in friends if name in neighbors]
print(friends_and_neighbors)

friends_lower = [n.lower() for n in friends]
print(friends_lower)
fn = [name.capitalize() for name in neighbors if name.lower() in friends_lower]