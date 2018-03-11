A = [9, 9, 9]

c = 0
last = 0
A[len(A) - 1] += 1
for i in reversed(range(len(A))):
    A[i] += c
    if A[i] >= 10:
        c = 1
        A[i] = 0
    else:
        c = 0

    last = i

if c != 0 and last != -1:
    A.insert(0, c)

print(A)
