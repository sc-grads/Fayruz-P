## YOUR CODE STARTS HERE:
# Start a while loop that calculates the sum of odd numbers from 1 to 100.
# Use my_sum variable to save the value
my_sum = 0
a = 100
while a:
    if a % 2 != 0:
        my_sum += a
    a -= 1

print(my_sum)
