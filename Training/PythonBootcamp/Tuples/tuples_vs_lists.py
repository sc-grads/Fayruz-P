# 1. Tuples are faster and more efficient than lists.

# 2. Tuples are safer than lists.

# 3. Tuples can be used as keys in dictionaries

# 4. Storage efficiency
import sys
l1 = [1, 2, 3, 4, 5, 6]
t1 = (1, 2, 3, 4, 5, 6)

print(f'List mem size: {sys.getsizeof(l1)}')
print(f'Tuple mem size: {sys.getsizeof(t1)}')
