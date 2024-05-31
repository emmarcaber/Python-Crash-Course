class Car:
	"""A simple to attempt to represent a car."""

	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odomoter_reading = 0


	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()


	def read_odometer(self):
		"""Prints a statement showing the car's mileage."""
		print(f"This car has {self.odomoter_reading} miles on it.")


	def update_odometer(self, mileage):
		"""
		Set the odometer reading.
		Reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odomoter_reading:
			self.odomoter_reading = mileage
		else:
			print("You can't roll back an odometer!")


	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odomoter_reading += miles


	def fill_gas_tank(self):
		"""Remind to fill the gas tank."""
		print("Please fill the gas tank.")


class Battery:
	"""A simple attempt to model a battery for an electric car."""

	def __init__(self, battery_size=75):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size


	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size}-kWh battery.")


	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315

		print(f"This car can go about {range} miles on a full charge.")


	def upgrade_battery(self):
		"""
		Check the battery size.
		Set the capacity to 100 if isn't already.
		"""
		self.battery_size = 100


class ElectricCar(Car):
	"""Represents aspects of a car, specific to a electric vehicles."""

	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an electric car.
		"""
		super().__init__(make, model, year)
		self.battery = Battery()


	def fill_gas_tank(self):
		"""Electric cars don't have gas tanks."""
		print("This car doesn't have gas tank!")


my_tesla = ElectricCar("tesla", "model s", 2019)
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# Upgrade the battery
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()