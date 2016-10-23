class Dog():
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def sit(self):
		print(self.name.title() + " is sitting.")

	def roll_over(self):
		print(self.name.title() + " is rolling over.")


my_dog = Dog('willie',6)

print("My dog's name is " + my_dog.name.title())
print(my_dog.name.title() + "'s age is " + str(my_dog.age))

my_dog.sit()
my_dog.roll_over()

my_dog2 = Dog('ron','8')
print("My dog's name is " + my_dog2.name.title())
print(my_dog2.name.title() + "'s age is " + my_dog2.age)

my_dog2.sit()
my_dog2.roll_over()
