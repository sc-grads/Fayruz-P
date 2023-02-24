l1 = [1, 2, 3]
l2 = l1
l2[0] = 'XX'
l2.append(10)
print(l1)
print(l2)

l3 = l1.copy()
l3.append('abc')


# 2.
nums = [1, 2, 3, 4, 5, 6, 7, 0, 1, 2]

#This is wrong!
# for n in nums:
#     if n < 5:
#         nums.remove(nums)
#
# print(nums)

new_list = list()
for n in nums:
    if n >= 5:
        new_list.append(n)
print(new_list)
