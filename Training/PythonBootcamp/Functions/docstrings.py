print(len('Python is cool'))


def say_hello(name):
    """This function says hello to you!

    The parameter will be concatenated to string Hello.
    The function does not return explicitly."""
    print(f'Hello{name}! :)')


say_hello('Fayruz')
help(say_hello)
print(say_hello.__doc__)
