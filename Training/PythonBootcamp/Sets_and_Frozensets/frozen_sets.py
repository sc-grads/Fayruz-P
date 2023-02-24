fs1 = frozenset({1, 2, 3, 'a', 'b'})
print(fs1, type(fs1))

s1 = 'Python is cool!!'
fs2 = frozenset(s1)
print(fs2)

fs3 = frozenset()

fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([3, 4, 5, 6])
fs3 = fs1.intersection(fs2)
print(fs3)

s1 = {4, 10, 20}
result1 = s1.intersection(fs1)
result2 = fs2 = s1

print(f'result1 type: {type(result1)}') # type set
print(f'result2 type: {type(result2)}') # type frozenset