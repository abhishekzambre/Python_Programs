class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for i in range(3, -1, -1):
            print(i)


obj = Solution()

arr = [0, 2, 3, 4]
arr2 = [0, 0]

print(obj.productExceptSelf(arr))

#print(obj.productExceptSelf(arr2))
