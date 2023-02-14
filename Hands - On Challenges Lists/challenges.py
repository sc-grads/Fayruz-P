# Challenge #1
#
# Create a Python script that removes all the occurrences of a given element of a list.

l1 = [1, 2, 1, 1, 2, 3, 1, 5, 3, 5, 1]
x = 2
while x in l1:
    l1.remove(x)

print(l1)
# Challenge #2
#
# Create a Python script that removes all the elements of a list that are duplicates.
l2 = [1, 2, 1, 2, 3, 4, 5, 5, 6, 3, 7]
new_list = []
for item in l1:
    if item not in new_list:
        new_list.append(item)

print(new_list)
#
# Challenge #3
#
# Consider the following string: nums = '10,20,30,40,50'
# Create a Python script that creates a list of integers from the string.
# The resulting list will be: [10, 20, 30, 40, 50]

nums = '10,20,30,40,50'
nums_list = nums.split(',')
print(nums_list)  # => ['10', '20', '30', '40', '50']

#
# Challenge #4
#
# Write a Python script that finds all numbers that are divisible by 7 but are not a multiple of 5, between 1500 and 3200 (both included).
#
# The numbers obtained should be printed in a comma-separated sequence (CSV) on a single line.

nums = list()

for i in range(1500, 3201):
    if i % 7 == 0 and i % 5 != 0:
        nums.append(str(i))

print(','.join(nums))

#
#
# Challenge #5
#
# Write a program that prompts the user for a long string containing multiple words separated by whitespaces and prints back the same string with the words in backward order.
#
# For example, say I type the string: My name is Andrei
#
# Then the script should print out: Andrei is name My

n = input('Enter a sentence:')
str_words = n.split(' ')
l6 = ''.join(reversed(str_words))
print(l6)

# Challenge #6
#
# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
#
# Sample input string : green-red-yellow-black-white
#
# Expected Result : black-green-red-white-yellow
#
string = input("Enter a hyphen-separated string: ")
words = string.split("-")
sorted_words = sorted(words)
sorted_str = "-".join(sorted_words)

print(sorted_str)

# Challenge #7
#
# Write a Python program that accepts as input a sequence of words separated by one or more whitespaces
# and prints out the same words with the letters in reversed order. Do not use list comprehension.
#
# Sample input string: I love cat and dogs
#
# Expected Result: I evol tac dna sgod
#
string = input("Enter a few words separated by whitespaces: ")
words = string.split()

# reverse the letters in each word
i = 0
for w in words:
    words[i] = w[::-1]
    i += 1

new_str = ' '.join(words)

print(new_str)


#
# Challenge #8
#
# Create an alternative solution for the previous challenge using list comprehension.

string = input("Enter a few words separated by whitespaces: ")
words = string.split()

# reverse the letters in each word
words = [w[::-1] for w in words]

new_str = ' '.join(words)

print(new_str)

#
#
# Challenge #9
#
# Create a Python script that calculates and displays the number of occurrences of each element of a list.
#
# Sample list: list('mamma mia mm')
#
# Expected Result:
#
# m ---> 6
#
# a ---> 3
#
# ---> 2
#
# i ---> 1
#
l1 = list('mama mia mm')
tmp_list = list()
for item in set(l1):
    count = l1.count(item)
    tmp_list.append((item, count))

# sort list by the second element of the tuple
tmp_list.sort(key=lambda x:x[1], reverse=True)
# print(tmp_list)

for item in tmp_list:
    print(f'{item[0]} ---> {item[1]}')

#
#
# Challenge #10
#
# Consider a list of words(strings). Write a Python script that generates a list of tuples where the first element of the tuple is the word in the list and the second element is its length.
#
# Use list comprehension if possible.
#
# Sample List: words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
#
# Expected Result: [('Python', 6), ('Java', 4), ('C++', 3), ('Golang', 6), ('Solidity', 8), ('Bash', 4)]


words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']

words_and_length = [(w, len(w)) for w in words]

print(words_and_length)