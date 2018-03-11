a = {1, 2, 1, 2}
b = {'a': 1, 'b': 2}

print(a)
print(b)

print(divmod(123, 10))
print(hash('asdf'))

l = [1, 2, 3]

i = iter(l)

print(next(i))
print(next(i))
print(next(i))

def factors(n):
    for k in range(1, n+1):
        if n % k == 0:
            yield k


for i in factors(10):
    print(i)

def fib():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a+b
        #a = b
        #b = future

print("Fibonacci")

for i in fib():
    print(i)
    if i > 100:
        break

d = {1: 0, 2: 3}

num = [1,2,3,4,5,6]

print(str(num)[1:-1])