def findTheDifference(s, t):
    s_l = list(s)
    for c in t:
        if c in s_l:
            s_l.remove(c)
        else:
            return c


print(findTheDifference("a", "aa"))
