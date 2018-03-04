import random

class Solution(object):


    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self._nums = nums[:]
        self._orig = nums[:]
        self._shuffle = []
        self._indexes = []

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self._orig

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self._nums)):
            ind = random.randint(0, len(self._nums) - 1)
            self._shuffle.append(self._nums[ind])
            self._indexes.append(ind)
            del self._nums[ind]
        return self._shuffle


obj = Solution([1, 2, 3])
print(obj.shuffle())
print(obj.reset())
