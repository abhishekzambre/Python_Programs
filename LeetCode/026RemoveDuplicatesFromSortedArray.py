class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0

        for i, n in enumerate(nums):
            print(i, n)


        return count

obj = Solution()
in_list = [1, 1, 2, 3, 3, 4, 5]
print(obj.removeDuplicates(in_list))
