t1 = tuple(range(20))
print(t1)

x = 10 # global scope
def my_func():
    global x
    x += 1
    print(x)



my_func()
print(x)

