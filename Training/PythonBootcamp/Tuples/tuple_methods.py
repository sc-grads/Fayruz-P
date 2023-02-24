t1 = (1, 2, 1, 3, 4)

# 1. tuple.index()
i = t1.index(2)
print(f'2 is at pos {i}')

# i = t1.index('x') # ERROR
x = 10
if x in t1:
    i = t1.index(x)
    print(f'x is at index{i}')
else:
    print(f'{x} not in tuple')

# 2. tuple.count()
n = t1.count(1)
print(n)

print(100 in t1)


# len(), sum(), max(), min(), sorted()
print(len(t1))
print(sum(t1))
print(max(t1))
print(min(t1))

t2 = sorted(t1, reverse=True)

