def singleNonDuplicate(nums):
    start = 1
    end = len(nums) - 2

    while start <= end:
        # mid = (start + end) // 2
        mid = start + ((end - start) // 2)
        if (nums[mid-1] == nums[mid]) or nums[mid+1] == nums[mid]:
            return True
        elif target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False


out = singleNonDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(out)
