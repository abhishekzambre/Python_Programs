class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la = len(a)
        lb = len(b)

        lm = max(la, lb)

        out = [0] * lm
        c = 0

        for i in range(lm-1, -1, -1):
            print(a[i])
            print(b[i])

            sum = int(a[i]) + int(b[i]) + c
            if sum > 1:
                out[i] = 0
                c = 1
            else:
                out[i] = sum
                c = 0

        if c == 1:
            out.insert(0, 1)

        return out


obj = Solution()
a = [1, 1]
b = [1]

print(obj.addBinary(a, b))