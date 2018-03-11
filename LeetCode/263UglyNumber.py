import math


class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num <= 0:
            return False

        factors = set()

        while num % 2 == 0:
            factors.add(2)
            num //= 2

        for i in range(3, int(math.sqrt(num)) + 1, 2):
            while num % i == 0:
                factors.add(i)
                num //= i

        if num > 2:
            factors.add(num)

        if bool(factors.difference({3, 2, 5})):
            return False
        else:
            return True

    def isUgly2(self, num):
        for i in [2, 3, 5]:
            while num % i == 0 < num:
                num //= i

        return num == 1


obj = Solution()
print(obj.isUgly(-234))
