a=[1,2,2,4,5,7,7,7,8,9]
b=[1,2,2,5,8]

print (*a)
print (*b)

i=0
j=0
m=len(a)
n=len(b)

flag=False
found=False
counter=0
steps=0

while (i < m):
	j=0
	steps+=1
	while(j < n):
		if(a[i]==b[j]):
			counter=counter+1
			print("a[", i, "], b[", j, "] --- ", a[i], ",", b[j])
			j=n
			steps+=1
		j=j+1
		steps+=1
	i=i+1
	if (counter == n):
		i=m

if(counter==n):
	print("Sequence Found")
else:
	print("Sequence not found")

print("Steps taken : ", steps)