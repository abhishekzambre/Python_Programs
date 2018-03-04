from itertools import combinations

def combinationSum3(k, n):

    out = []

    for i in list(combinations(range(1, 10), k)):
        if sum(i) == n:
            out.append(list(i))

    return out


print(combinationSum3(3, 7))

print(combinationSum3(3, 9))
