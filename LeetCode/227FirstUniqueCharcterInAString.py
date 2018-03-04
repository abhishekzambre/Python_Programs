def firstUniqChar(s):

    dict = {}

    for c in s:
        dict[c] = 1 + dict.get(c, 0)

    for i, c in enumerate(s):
        if dict[c] == 1:
            return i

    return -1


print(firstUniqChar("loveleetcode"))
print(firstUniqChar("leetcode"))
