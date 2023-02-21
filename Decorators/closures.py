#################################
## Inner Functions and Closures
#################################

# A function defined inside another function is called  nested or inner function.
# Inner functions can access variables of the enclosing scope and become closures.


# defining an outer function
def outer():
    msg = 'Python'
    x = 0

    # defining an inner function
    def inner():
        # nonlocal is used to declare that a variable inside a nested function
        # is not local to it (it lies in the outer enclosing function).
        nonlocal x  # this is `x` from outer function
        x += 1
        print(f'{msg} is really cool!')  # `msg` and `x` are free variables
        return x

    return inner


func1 = outer()
print(type(func1))  # => <class 'function'>

xx = func1()
print(xx)  # => 1

print(func1())  # => 2
print(func1())  # => 3
print(func1())