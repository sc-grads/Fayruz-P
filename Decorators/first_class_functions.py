def sum(number, fn):
    result = 0
    for n in range(1, number+1):
        result += fn(n)

    return result

def square(x):
    return x ** 2
result = sum(3,square)
# 1 + 4 + 9
print(result)

import math
result = sum(10, math.sqrt)
print(result)

# function that returns a function
def compute(msg):
    if msg == "sqaure":
        return square
    else:
        return math.sqrt

func = compute("square")

func = compute("square")
print(type(func))
print(func(10))

fn = compute("x")
print(fn(25))
