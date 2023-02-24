# For Loops
# Using a for loop and the range() function, calculate the sum and the product of the numbers between 1 and 25  (both included).
#
# Store the calculated values in two variables called my_sum and my_product.
#
# Print the values of my_sum and my_product variables.

my_sum = 0
my_product = 1

for i in range(1, 26):
    my_product *= i
    my_sum += i

print(my_sum, my_product)
