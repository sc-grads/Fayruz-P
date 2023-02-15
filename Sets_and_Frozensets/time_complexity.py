import time
import sys

l1 = list(range(1_000_000))
start = time.time()
# print(start)
bv = 54653 in l1
end = time.time()
print(f'List loopup time: {end - start:.10f}')
print('#' * 50)
