# *args

def average(a, b, *args):
    # print(f'args is {args}')
    return (a + b + sum(args)) / (2 + len(args))


def concatenate(*args):
    result = ''
    for tmp in args:
        result = result + tmp
    return result


# print(average(4, 5, 6, 7))
r = concatenate(('Python', '3', '!'))
print(r)

result = concatenate('I', 'Love', 'Programming')
print(result)
