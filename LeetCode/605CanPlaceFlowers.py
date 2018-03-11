class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        for i in range(0, len(flowerbed)-2):
            if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i+2] == 0:
                print("Place", i)
                i += 3


        return True


obj = Solution()

print(obj.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))
