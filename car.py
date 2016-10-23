class Car():

	def __init__(self, make, model, year):
		self.make=make
		self.model=model
		self.year=year
		self.odometer_reading = 0

	def get_name(self):
		long_name = self.make + " " + self.model + " " + self.year
		return long_name.title()

	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")
	
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		self.odometer_reading += miles

class Battery():
	def __init__(self,battery_size=70):
		self.battery_size=battery_size

	def describe_battery(self):
		print("Battery size is " + str(self.battery_size))


class ElectricCar(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery = Battery()
