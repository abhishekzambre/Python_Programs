class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        start = 0
        end = len(s) - 1

        longest = s[0]

        print(start, end, longest)

        cur_start = start
        cur_end = end

        while cur_start <= cur_end:

            if s[cur_start] == s[cur_end]:
                print("found at:", cur_start, cur_end)
            else:
                cur_end -= 1

        return "asdf"


obj = Solution()

print(obj.longestPalindrome("baaad"))
