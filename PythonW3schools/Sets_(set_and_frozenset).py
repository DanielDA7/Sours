#data = set(("apple", "banana", "cherry"))
data = {5, 3, 7, 1 ,5}

data.add(9)
data.update([11, 13, 15])
print(data)
data.remove(3)
print(data)

nums = {1, 2, 3, 4, 5}
new_nums = set(nums)
print(new_nums)


new_data = frozenset([5,2,5,6,'7', True, False])

print(new_data)