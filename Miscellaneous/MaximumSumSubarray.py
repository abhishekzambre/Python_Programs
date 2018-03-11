def findMaxSum(nums):
    best = 0
    total = 0

    for i in nums:
        print(i, total+i, best)
        total = max(i, total+i)
        best = max(best, total)

    return best


out = findMaxSum([-1, 2, 4, -3, 5, 2, -5, 2])

print(out)