nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))
print(nums[:2])

a = 7
b = 42

a, b = b, a
print(a,b)