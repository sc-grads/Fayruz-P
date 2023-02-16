#
# Challenge #1
#
# Consider this text file that contains multiple duplicate MAC addresses.
#
# Create a new file that contains only unique MAC addresses. Each MAC should be on its own line.
with open('macs.txt') as f:
    content = f.read().split()
    # print(content)

    # eliminating duplicates
    content = list(set(content))
    print(content)

# writing to file
with open('mac_unique.txt', 'w', newline='') as f:
    for mac in content:
        f.write(f'{mac}\n')
#
# Challenge #2
#
# Create a Python script that reads a text file into a list and then converts the list into a string that has the entire file content.
#
with open('sample_file.txt', 'r') as f:
    content = f.read().splitlines()
    content = list(content)

    for item in content:
        my_str = '\n'.join(content)
        print(my_str)

# Challenge #3
#
# Create a Python script that removes all empty lines including those that contain only spaces from a file.
#
while open('file.txt', 'r') as f:
    content_list = f.readlines()


# create a new list eliminating the elements that are empty strings or contain only spaces
tmp_list = [line for line in content_list if line.strip() != '']
print(tmp_list)

# write to a new file
with open('file_without_blanks.txt', 'w') as f:
    f.write(''.join(tmp_list))
#
# Challenge #4
#
# Create a Python function called tail that reads the last n lines of a text file. The function has two arguments: the file name and n (the number of lines to read). This is similar to the Linux `tail` command.
#
# Example: tail('sample_file.txt', 5) will return the last 5 lines from sample_file.txt.

# create a new list eliminating the elements that are empty strings or contain only spaces
tmp_list = [line for line in content_list if line.strip() != '']
print(tmp_list)

# write to a new file
with open('file_without_blanks.txt', 'w') as f:
    f.write(''.join(tmp_list))
# Challenge #5
#
# Change the solution from the previous challenge so that the script that prints out the last n lines of the file refreshes the output every 3 seconds (as the file changes or updates). This is similar to the tail -f Linux command.
import time
def tail(file, n):
    with open(file, 'r') as f:
        # reading the file in a list
        content = f.read().splitlines()
        # getting the last n elements of the list
        last = content[len(content)-n:]
        # print(last)
        # concatenating the list back into a string
        my_str = '\n'.join(last)
        return my_str

while True:
    t = tail('sample_file.txt', 3)
    print(t)
    time.sleep(3)
    print('')
#
#
# Challenge #6
#
# Write a Python program to count the number of lines, words, and characters in a text file. This is similar to the Linux `wc` command. Create a function, if possible.

def c(file):
    with open('sample_file.txt', 'r') as f:
        content = f.read().splitlines()

        lines = len(content)

        words = 0
        for line in content:
            words += len(line.split())

        chars = 0
        for line in content:
            chars += len(list(line))

        return lines, words, chars

    print(wc('sample_file.txt'))
#
#
# Challenge #7
#
# Write a Python program that calculates the net amount of a bank account based on the transactions that are saved in a text file.
#
# The file format is as follows:
#
# D:50
#
# W:100
#
# D means deposit while W means withdrawal.
#
# Suppose that the following file is supplied to the program:
#
# D:300
#
# D:300
#
# W:500
#
# D:200
with open('banking.txt', 'r') as f:
    content = f.read().splitlines()
    # print(content)

    deposit, withdrawal = 0, 0

    for item in content:
        tmp = item.split(':')
        # print(tmp) # -> ['D', '300']
        if  tmp[0] == 'D':
            deposit += int(tmp[1])
        elif tmp[0] == 'W':
            withdrawal += int(tmp[1])
        else:
            print('File format error')

    balance = deposit - withdrawal
    print(balance)


# Challenge #8
#
# Write a Python script that compares line by line two text files and displays the lines that differ.

with open('a.txt') as f:
    file1 = f.read().splitlines()

with open('b.txt') as f:
    file2 = f.read().splitlines()

file = list(zip(file1, file2))

i = 0
for item in file:
    i += 1
    if item[0] != item[1]:
        print(f'file1 ({i}): {item[0]}, file2 ({i}): {item[1]}')

#
#
# Challenge #9
#
# Consider this dictionary file.
#
# Write a Python script that reads the file in a dictionary. The words in the file will be the dictionary keys and the length of each word the corresponding values.
#

with open('american-english.txt') as f:
    words = f.read().splitlines()


    words_and_length = dict()
    for w in words:
        words_and_length[w] = len(w)

    for k, v in words_and_length.items():
        print(f'{k} -> {v}')

#
# Challenge #10
#
# Consider the dictionary file from the previous challenge.
#
# Write a Python script that finds the first 100 longest words in the file.
with open('american-english.txt') as f:
    words = f.read().splitlines()

    words_and_length = dict()
    for w in words:
        words_and_length[w] = len(w)

    words_list = sorted(words_and_length.items(), key=lambda x: x[1], reverse=True)
    print(words_list[:100])
#
#
# Challenge #11
#
# Consider this dictionary file.
#
# Write a Python script that finds the number of occurrences of each letter of the alphabet in all the words of the dictionary. Make a distinction between lower and uppercase letters.
#
# You want to see how many times 'a', 'A', 'b', 'B', 'c', 'C', 'd' and so on appear in all the words in the dictionary.
#
import string

letters = dict()

# initializing the dictionary with all letters as keys and zero as values
for c in string.ascii_letters:
    letters[c] = 0

# print(letters)

with open('american-english.txt', 'r') as words:
    for w in words:
        for char in string.ascii_letters:
            letters[char] += w.count(char)

print(letters)
#
#
# Challenge #12
#
# Change the solution from the previous challenge so that the script considers all letters lowercase (it makes no distinction between lower and uppercase letters).

import string

letters = dict()

# initializing the dictionary with all letters as keys and zero as values
for c in string.ascii_lowercase:
    letters[c] = 0

# print(letters)

with open('american-english.txt', 'r') as words:
    for w in words:
        for char in string.ascii_lowercase:
            letters[char] += w.lower().count(char)  # work on a lowercase copy of w

print(letters)

#
# Challenge #13
#
# Continue the previous challenge and find the 3 most frequently used letters in all English Words.
#

import string

letters = dict()

# initializing the dictionary with all letters as keys and zero as values
for c in string.ascii_lowercase:
    letters[c] = 0

# print(letters)

with open('american-english.txt', 'r') as words:
    for w in words:
        for char in string.ascii_lowercase:
            letters[char] += w.count(char)



print(sorted(letters.items(), key=lambda x:x[1], reverse=True))
