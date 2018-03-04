def strtoint(s):

    out = 0
    neg = 1

    for c in s:
        if c == "-":
            neg = -1
        else:
            out += (ord(c) - 48)
            out *= 10

    return neg * (out//10)


out = strtoint("-100000")

print(type(out), out)
