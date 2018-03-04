def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    dict = {}
    for i, num in enumerate(numbers):
        if num in dict:
            return dict[num] + 1, i + 1
        else:
            dict[target - num] = i


print(twoSum([2, 7, 11, 15], 9))

print(twoSum([2, 3, 4], 6))
