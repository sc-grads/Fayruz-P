n = len([1, 2, 4, 5])
print(n)


def add1(a, b):
    print(f'Sum: {a + b}')


def add2(a, b):
    return a + b


def func1():
    pass


add1(10, 20)
my_sum = add2(5, 2)
print(my_sum)

x = func1()
print(x)
print(add1(1, 2))


def my_func(x):
    return x, x ** 2, x ** 3, x ** 4


print(my_func(3))
a, b, c, d = my_func(10)
print(a, b, c, d)
x, *y = my_func(4)
print(x, y)
