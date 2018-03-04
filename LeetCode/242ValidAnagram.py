import time

def isAnagram(s, t):

    count_dict = {}

    for c in s:
        count_dict[c] = 1 + count_dict.get(c, 0)

    for c in t:
        count_dict[c] = count_dict.get(c, 0) - 1
        if count_dict.get(c, -1) == 0:
            count_dict.pop(c)

    return True if not count_dict else False


def isAnagram2(s, t):
    index = [0] * 26
    for c in s:
        index[ord(c) - 97] += 1

    for c in t:
        index[ord(c) - 97] -= 1

    for i in index:
        if i != 0:
            return False

    return True

timer = time.time()
print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
print(time.time() - timer)


timer = time.time()
print(isAnagram2("anagram", "nagaram"))
print(isAnagram2("rat", "car"))
print(time.time() - timer)