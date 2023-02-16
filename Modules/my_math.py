a = 10
def my_sum(*args):
    s = 0
    for number in args:
        s = s + number
    return s

print('Message printed inside my_path.py')
s = my_sum(10,20,30)
print(f'sum is {s}')

print(f'__name__ in my_math.py is {__name__}')
