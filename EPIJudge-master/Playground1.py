# from itertools import compress
#
# print(~True)
# print(~False)
#
# print(int(True))
# print(bin(1))
# print(bin(-1))
#
# # print(sys.maxsize)
# # print(sys.float_info)
#
# print("{0:b}".format(5))
# print("{0}, {1:09b}".format(5, 19))
#
# c = "{0:09b}".format(10)
#
# print(c, type(c))
#
# d = -2
#
# e = "{0:05b}".format(d)
# print(e, "\n\n")
#
# d = d >> 2
#
# g = "{0:b}".format(64)
# e = "{0:b}".format(4)
#
# print("{0}, {1}".format(g, e))
# print("{0:b}".format(64 | 4))
# print("{0}".format(68 | 4))
#
# print("{0}".format(8 >> 1))
# print("{0}".format(1 << 4))
# print("{0}".format(~0))
#
# print(~1)
#
# print(15 ^ 10)
#
# n = [1, 2, 4, 6, 1, 2, 0, 9, 4]
#
# mask = [x > 4 for x in n]
#
# print("{0:010b}".format(58))
# print("{0:010b}".format(58-1))
# print("{0:010b}".format(58 & (~58+1)))
# print("last {0:010b}".format(58 & 58-1))
# print("{0:010b}".format(~58+1))
#
#
# print("{0:010b}".format(88))
print("{0:010b}".format(88 & (1 << 2)))
print("{0:010b}".format(88 ^ (1 << 4)))
#
# if -7 & 1 == 0:
#     print("Even")
# else:
#     print("Odd")

import time

from collections import Counter
from collections import deque

x = time.time()

if 12305496 & 1 == 0:
    print("Even")
else:
    print("Odd")

print("{0:2f}".format(time.time() - x))

x = time.time()

if 12305496 % 2 == 0:
    print("Even")
else:
    print("Odd")

print("{0:2f}".format(time.time() - x))


l1 = ["A", "B", "A", "A", "B", "C", "D", "D", "D"]

l2 = ["A", "B", "A", "A", "B", "C", "D", "D", "D", "E", "A"]

c = Counter(l1)
d = Counter(l2)
print(c)
print(d)
print(c | d)


q = deque()

q.appendleft("first")
q.appendleft("second")
q.append("zeroth")

print(q)

q.pop()

print(q)

q.popleft()

print(q)

d = {"asdf": 3.5}

print(d.setdefault("asdfe", 4))

print(d.get("asdfe", 0))

print(d)

from collections import namedtuple

coord = namedtuple("Coordinates", ['x', 'y'])

c = coord(y=4, x=1)

print(c.x)
print(c[1])

print(c._make([3, 4]))

print(c)