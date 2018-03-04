class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for j in J:
            for s in S:
                if (j == s):
                    count += 1
        return count

    def numJewelsInStones2(self, J, S):
        setJ = set(J)
        return sum(s in setJ for s in S)


s = Solution
print(s.numJewelsInStones(s, "aA", "aAAbbbb"))
print(s.numJewelsInStones2(s, "aA", "aAAbbbb"))
