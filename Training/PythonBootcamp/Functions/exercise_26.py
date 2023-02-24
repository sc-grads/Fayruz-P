# Global variable, initialize it with whatever value you want
x = 10


def increment():
    global x
    x += 1


## Call the function

increment()
print(x)
## Print x


