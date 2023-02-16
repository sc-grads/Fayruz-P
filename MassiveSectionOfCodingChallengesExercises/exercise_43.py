
# List with duplicates
years = [2010, 2010, 2011, 2011, 2012, 2012, 2012]

# New list with unique elements
years_unique = []

# YOUR CODE STARTS HERE
[years_unique.append(item) for item in years if item not in years_unique]
