def customSortString(S, T):
    out = ""
    for c in S:
        out += c * T.count(c)
    for c in set(T).difference(set(S)):
        out += c * T.count(c)
    return out


customSortString("cba", "asbdc  ")