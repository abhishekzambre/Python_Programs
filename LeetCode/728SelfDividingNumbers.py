class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        out = []

        for i in range(left, right+1):
            if self.isselfdivide(i):
                out.append(i)

        return out

    def isselfdivide(self, n):

        temp = n

        while temp != 0:
            dig = temp % 10
            if dig == 0 or n % dig != 0:
                return False
            temp = temp // 10

        return True

obj = Solution()

print(obj.selfDividingNumbers(9, 28))