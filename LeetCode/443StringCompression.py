class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        size = len(chars)-1
        init_pos = 1
        init_count = 1
        for i in range(size):
            print(i, size, chars[i], chars[i+1])
            if i < size and chars[i] == chars[i+1]:
                init_count += 1
            else:
                if init_count > 1:
                    chars[i] = str(init_count)
                    init_pos += 2
                    init_count = 1

        print(init_pos, init_count)
        chars[init_pos] = str(init_count)

        return chars


obj = Solution()

#print(obj.compress(["a"]))
print(obj.compress(["a", "a", "b", "b", "c", "c", "c"]))
print(obj.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
