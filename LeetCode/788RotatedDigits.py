class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """

        count = 0

        for n in range(1, N+1):
            num = str(n)

            if '3' in num or '7' in num or '4' in num:
                continue

            if '2' in num or '5' in num or '6' in num or '9' in num:
                count += 1

        return count

        # rotated = {'0': '0', '1': '1', '8': '8', '2': '5', '5': '2', '6': '9', '9': '6'}
        #
        # for n in range(1, N+1):
        #     orig = str(n)
        #     new = []
        #     for c in orig:
        #         if rotated.get(c, 0):
        #             new.append(rotated[c])
        #         else:
        #             break
        #
        #     if orig != ''.join(new) and ''.join(new) != "" and len(orig) == len(new):
        #         print(orig, new)
        #         count += 1
        #
        # return count


obj = Solution()
print(obj.rotatedDigits(13))
