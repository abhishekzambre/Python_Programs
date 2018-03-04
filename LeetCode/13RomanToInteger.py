class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0

        conv_table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        for i in range(len(s)-1):
            if conv_table[s[i]] < conv_table[s[i+1]]:
                total -= conv_table[s[i]]
            else:
                total += conv_table[s[i]]

        return total + conv_table[s[-1]]


obj = Solution()

print(obj.romanToInt("I"))
