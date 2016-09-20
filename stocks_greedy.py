a=[1,2,2,4,5,6,7,7,7,8,9]
b=[1,2,2,5,6,8]
k=[0,0,0,0,0,0,0,0,0,0,0,0]

print (*a)
print (*b)

i=0
j=0
m=len(a)
n=len(b)

while (i<m) and (j<n):
	if (a[i]==b[j]):
		k[j]=i
		i+=1
		j+=1
	else:
		i+=1

if (i+1 == m):
	print("Sequence found")
	print(*k)
else:
	print("Sequence not found")