def moveZeros(nums):
    zero = 0
    for i in range(len(nums)):
        print(nums, "i", i, "zero", zero)
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1

    print(nums)


print(moveZeros([8, 0, 9, 8, 0, 0, 7]))
