def reverseString(s):
    rs = []
    rl = len(s)
    for i in range(rl):
        rs.append(s[rl-i-1])
    return ''.join(rs)


print(reverseString("asdfdf"))
