nums = [3, 2, 4]
sum = 6
i, j = 0, 0

dict = {}

for i, n in enumerate(nums):

    if (n in dict.keys()):
        print(dict.get(n), i)
        break
    dict[sum - n] = i
print(dict)