#List Concatenation

l1 = [3, 4]
print(l1, id(l1))
l1 = l1 + [5,6]
print(l1, id(l1))

l1 += [7,8]
print(l1,id(l1))

l1.extend([11,12])
print(l1,id(l1))

l1.append(['a', 'b'])
print(l1)
l1.extend(['x', 'y'])
print(l1)
l1.append(20)
l1.extend([20])
print(l1)
# l1.extend(20) # ERROR

l2 = list('abc')
l3 = l2 * 3
print(l3)

print('#' * 10 + ' LIST SLICING' + '#' * 10)
numbers = [1, 2, 3, 4, 5]
nums = numbers[1:4]
print(f'nums: {nums}')
print(f'nums: {numbers}')
print(numbers[:3])
print(numbers[2:])
print(numbers[1:5:3])
print(numbers[4:1:-2])
print(numbers[::])
print(numbers[::-1])
print(numbers[1:100])
numbers[0:2] = ['a', 'b']
print(numbers)

print('#' * 10 + ' LIST ITERATION' + '#' * 10)
ip_list = ['125', '157', '548']
for ip in ip_list:
    print(f'Connecting to {ip}....')

print('458'not in ip_list)
