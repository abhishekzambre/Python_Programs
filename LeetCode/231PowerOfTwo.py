class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False
        while n != 1:
            if n % 2 != 0:
                return False
            n //= 2
        return True

    def isPowerOfTwo2(self, n):
        if n <= 0:
            return False
        return not(n & (n-1))


obj = Solution()

print(obj.isPowerOfTwo(0))

print(obj.isPowerOfTwo2(17))
