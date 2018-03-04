# palindrome checker

s="asda"

print(s)

print(s[1])

print(all(s[i]==s[len(s)-1-i] for i in range(len(s)//2)))

for i in range(len(s)//2):
	if( s[i] == s[len(s)-1-i] ):
		print("True")
	else:
		print("False")