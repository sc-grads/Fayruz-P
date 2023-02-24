f = open('a.txt', 'r')

# Move the cursor on position 4 inside the file
f.seek(4)

# Read 5 characters starting with position 4 and return them in variable called word
word = f.read(5)
print(word)  # => first

# Closing the file
f.close()