#  lambda parameter_list: expression

def add(a, b, c):
    result = a + b + c
    return result

result = (lambda a,b, c: a +b +c )(3, 4, 5)
print(result)

square = lambda x=10: x ** 2
print(square(4))
print(square())

friends = [('Diana', 30), ('Ana', 25) ('Tudor', 22)]
friends.sort(key=lambda x: len(x[0]))
print(friends)

