class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        decimal = 0
        out_bin = []
        while num != 0:
            out_bin.append(num % 2 ^ 1)
            num //= 2

        for i in reversed(out_bin):
            decimal = decimal * 2 + i

        return decimal