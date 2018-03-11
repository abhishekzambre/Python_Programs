class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a = set("qwertyuiop")
        b = set("asdfghjkl")
        c = set("zxcvbnm")

        out = []

        for word in words:
            t = set(word.lower())
            print(b, t, b & t, b & t == t)
            if a.issuperset(t) or b.issuperset(t) or c.issuperset(t):
                out.append(word)

        return out


obj = Solution()

print(obj.findWords(["Hello", "Alaska", "Dad", "Peace"]))
