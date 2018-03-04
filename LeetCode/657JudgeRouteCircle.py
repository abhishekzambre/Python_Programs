def judgeCircle(moves):
    h = v = 0

    for c in moves:
        if c == "U":
            v = v + 1
        elif c == "D":
            v = v - 1
        elif c == "R":
            h = h + 1
        else:
            h = h - 1

    if h == 0 and v == 0:
        return True
    else:
        return False


def judgeCircle2(moves):
    return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")

print(judgeCircle("UD"))
print(judgeCircle("LL"))
print(judgeCircle("ULDR"))
print(judgeCircle("DDRULLU"))
print(judgeCircle(""))
