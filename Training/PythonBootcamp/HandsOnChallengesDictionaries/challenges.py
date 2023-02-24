# # Challenge #1
# #
# # Create a Python script that removes all the elements of a list that are duplicates.
# #
# # Do the challenge in a single line of code using sets.
#
l1 = [1, 2, 3, 4, 2, 1, 3, 6, 7, 7]
l1 = list(set(l1))
print(l1)
#
# Challenge #2
#
# Consider a list of words (strings). Write a Python script that generates a dictionary where the key is the word in the list and the value is its length.
#
# Sample List: words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
#
# Expected Result: {'Python': 6, 'Java': 4, 'C++': 3, 'Golang': 6, 'Solidity': 8, 'Bash': 4}

words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
words_and_length = dict()

for w in words:
    words_and_length[w] = len(w)

print(words_and_length)
#
# Challenge #3
#
# Considering the following dict, get a dict representation sorted by key.
#
d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
d1 = sorted(d1.keys())
print(d1)
#
# Challenge #4
#
# Considering the following dict, get a dict representation sorted by value.
#
d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
d1 = sorted(d1.values())
print(d1)
#
#
# Challenge #5
#
# Let's generalize the last challenge and sort a dictionary by any field of its values if the value is a composite type (list, tuple, etc).
#
# Example: Considering this dictionary print a sorted view of the dictionary by the second field of its values.
#
employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
employees = sorted(employees.items())
print(employees)
#
#
# Challenge #6
#
# Consider this dictionary. Print a sorted view of the dictionary by the third field of its values, in reverse order.
#
employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
employees = sorted(employees.items(), key = lambda x:x[1][2],reverse=True)
# The output should be: [('Maria', ('Zagreb', 3800, 40)), ('Diana', ('NYC', 3500, 31)), ('John', ('London', 4000, 28))]
#
# Challenge #7
#
# Consider the dictionary called COUNTRY declared in this Python script.
#
# The keys are the country codes and the values are the country names.
#
# Print a sorted view of the dictionary, by the key (country code).
# keys = sorted(COUNTRY.keys())
# # print(keys)
#
# for k in keys:
#     print(f'{k} --> {COUNTRY[k]}')

#
# Challenge #8
#
# Consider the dictionary called COUNTRY declared in this Python script.
#
# Find the country which has the longest name.
#
# Use list comprehension if possible.

# list with the lengths of each countries

# lengths = [len(value) for value in COUNTRY.values()]
# print(lengths)
# m = max(lengths)  # the longest country name
# # print(m)
#
# cc = [c for c in COUNTRY.values() if len(c) == m]
# print(cc)   # -> ['SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA', 'SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS']
# #
#
#
# Challenge #9
#
# Consider the following two Python Lists that save information about company sales for the last 6 years:
#
years = [2015, 2016, 2017, 2018, 2019, 2020]

sales = [350000, 400000, 410000, 439000, 500000, 290000]
#
# Create a new list that connects the year to the corresponding sales.

l2 = list(zip(years,sales))
print(l2)

# The resulting list should be: [(2015, 350000), (2016, 400000), (2017, 410000), (2018, 439000), (2019, 500000), (2020, 290000)]
#
# Are you stuck? Do you want to see the solution to this exercise? Click here.
#
#
#
# Challenge #10
#
# Consider the following two Python Lists that save information about company sales for the last 6 years:

years = [2015, 2016, 2017, 2018, 2019, 2020]

sales = [350000, 400000, 410000, 439000, 500000, 290000]
#
# Create a new dictionary that has the keys, the years, and the values, the sales.

d3 = dict(zip(years,sales))
print(d3)
# The resulting dict should be: {2015: 350000, 2016: 400000, 2017: 410000, 2018: 439000, 2019: 500000, 2020: 290000}

#
#
# Challenge #11
#
# Consider the dictionary from the previous challenge.
#
# Create a new dictionary called profit that stores the profit of the company, if the profit margin is 25% of the sales.
#
# Use dictionary comprehension if possible.
years = [2015, 2016, 2017, 2018, 2019, 2020]
sales = [350000, 400000, 410000, 439000, 500000, 290000]

company_sales = dict(zip(years,sales))
# print(company_sales)

# profit margin is 25%
profit = {k: v*0.25 for k, v in company_sales.items()}
print(profit)

#
#
#
# Challenge #12
# #
# Consider the following 2 Lists:
names = ["Dan", "John", "Diana"]
phones = [11111, 2222, 3333]
#
# Create a set that contains the elements of the 2 lists in pairs.

s1 = set(zip(names,phones))
print(s1)

# The resulting set should be: {('John', 2222), ('Diana', 3333), ('Dan', 11111)}

#
# Challenge #13
#
# Consider the two Python lists. Write a Python Script to make a new list whose elements are the intersection of the two given lists. This means all elements of L1 that also belong to L2, but no other elements.
#

L1 = [1, 2, 5, 10, 11, -10, 9, 88]
L2 = [88, 5, 10, 6, 7]

L3 = list(set(L1).intersection(set(L2)))
print(L3)
#
#
# Challenge #14
#
# Write a Python script that validates an email address by writing "Valid email!" or "Invalid email!".
#
# If the email is not valid the script should display why it's not valid.
#
# We consider a valid email address if:
#
# it has at least 6 characters but no more than 16.
#
# it contains both . and @
#
# it does not contain any of the following characters:'[]{}()$*'
not_permitted = '[]{}()$*'
must_contain = '.@'
while True:
    email = input("Enter your email:")
    if len(email) < 6 or len(email) > 16:
        print('Invalid email length!')
    elif not set(email).isdisjoint(set(not_permitted)):  # two sets are disjoint if they have no elements in common
        print('Invalid symbols in email!')
    elif set(must_contain) & set(email) != set(must_contain):
        print('Invalid email. Must contain . and @')
    else:
      print('Valid email!')
      break