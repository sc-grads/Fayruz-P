# Identity Operators: "is" and "is not"

a, b = 3, 4
print(a is b)

# Immutable types: int, float, str, tuple, frozenset
# Mutable types: list, set, dict

print(id(a))
a += 3
print(a)
print(id(a))

numbers = [1, 2, 3]
print(id(numbers))
numbers.append(100)
print(numbers)
print(id(numbers))

nums = numbers.copy()
print(nums == numbers)
print(nums is numbers)
