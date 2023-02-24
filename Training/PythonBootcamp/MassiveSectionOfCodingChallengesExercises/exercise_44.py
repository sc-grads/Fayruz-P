# List of Words
words = ['Anna', 'Car', 'Civic', 'Screen', 'Level', 'Cat', 'Mom']

# YOUR CODE STARTS HERE

palindromes = [items for items in words if items.lower() == items[::-1].lower()]
