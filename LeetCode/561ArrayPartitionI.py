class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for i in sorted(nums)[::2]:
            total += i

        return total