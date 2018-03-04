A = [0,1,2,0,2,1,1]
print(A)

i=2
pivot = A[i]
print("Pivot : " + str(pivot))
for i in range(len(A)):
	for j in range(i+1, len(A)):
		if A[j] < pivot:
			A[i], A[j] = A[j], A[i]

print(A)

for i in reversed(range(len(A))):
	if A[i] < pivot:
		break
	for j in reversed(range(i)):
		if A[j] > pivot:
			A[i], A[j] = A[j], A[i]
			break