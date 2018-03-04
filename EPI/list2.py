#in place divide evens in first half, odds in second half of list

n=[3,3,3,3,2,2,2,2]
print(n)

min=0
max=len(n)-1

while(min<max):
	if(n[min]%2!=0):
		n[min], n[max] = n[max], n[min]
		max = max-1
	else:
		min = min+1

print(n)