from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        c = Counter(nums)
        return heapq.nlargest(k, c, c.get)


obj = Solution()

print(obj.topKFrequent([1, 1, 1, 2, 2, 3], 2))
