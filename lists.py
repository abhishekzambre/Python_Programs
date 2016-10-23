
available_toppings = ('mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese')

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print ("Adding " + requested_topping)
	else:
		print ("Sorry, we don't have " + requested_topping)




'''
bikes = ['hero', 'tvs', 'suzuki','ducati','kawasaki']
models = ['splender', 'apache', 'honda']

bikes2=[]

if bikes2:
	print("List full")
else:
	print("Add items")

if 'tvs1' in bikes:
	print("good")
elif 'suzuki1' in bikes:
	print("ok") 
else:
	print("not good")

for bike in bikes:
	if bike == 'tvs':
		print (bike.upper())
	else:
		print (bike.title())

bikes2=bikes

bikes.append('temp1')
bikes2.append('temp2')

print(bikes)
print(bikes2)


alphas=('a','b','c')

for alpha in alphas:
	print (alpha)

x=0
y=0

print(bikes)
x=int(input("Which was your first bike make : "))

print(models)
y=int(input("Which was your first bike model :"))

print("Your first bike was " + bikes[x].title() + " " + models[y].title())

bikes[0]="hero"

bikes.append("yamaha")

bikes.insert(1, "ducati")
del bikes[0]

print(bikes)

x=bikes.pop(0)

print(bikes)

print(x)

print(bikes)

bikes.remove("tvs")

print(bikes)

bikes.sort(reverse=False)


print(bikes)

#print(sorted(bikes))

#bikes.reverse()

#print(len(bikes))

for bike in bikes:
	print(bike)

x = list(range(1,10,2))

print(x)

squares=[]

for value in range(1,10):
	sqaure=2**value
	squares.append(sqaure)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))


sq=[2**value for value in range(1,10)]
print(sq)
'''

