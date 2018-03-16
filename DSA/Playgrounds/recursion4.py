import sys

def fib(n):
	fib(n)

#fib(10)

print(sys.getrecursionlimit())


def linear_sum(S,n):
	return 0 if n==0 else linear_sum(S, n-1) + S[n-1]
	
print(linear_sum([1,2,3,4,5,6],6))