def lengthOfLongestSubstring(s):
    longest = 1
    current = 0
    A = set()
    if (s == ""):
        print("lol")
        return
    for i in s:
        print(i, current)
        if (i in A):
            if (current >= longest):
                longest = current
            current = 0
        current += 1
        A.add(i)

    print(A)
    print(longest)


lengthOfLongestSubstring("au")