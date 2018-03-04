import copy

a = [1] * 2 + [0] * 5 + [3]

b = list(range(15))

print(a)

print(b)

print(len(b))

b.append(12)
a.remove(0)
print(a)

print(b)


c = b

d = [[1, 2], [3, 4, 5], [6]]

print(c)

e = list(d)
f = d

print(d)

print(e)

print(f)

print("-----------")

ab = [1, 2, 3, 4, 5]
print(ab)

cd = ab
ef = copy.copy(ab)
gh = copy.deepcopy(cd)
cd.remove(2)

print(ab)
print(ef)
print(gh)

print("-----------")

print(b)
print(b[2:6])
print(b[0:10:2])
print(b[-7:-4])
print(b[10:2:-2])
print(list(reversed(b)))
print(b[4:2:-1])


A = [1,6,3,4,5,2,7]
print(A)

A = A[2:] + A[:2]
print(A)


print([x**2 for x in range(6) if x%2==0])

