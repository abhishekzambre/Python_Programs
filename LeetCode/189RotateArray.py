class Solution:
    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        k = k % n

        nums[:] = nums[n-k:] + nums[:n-k]

        print(nums)

    def rotate2(self, nums, k):


        pass

obj = Solution()
obj.rotate1([1, 2, 3, 4, 5, 6, 7], 3)
obj.rotate1([1, 2], 1)
