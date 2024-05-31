# Storing Multiple Classes in a Module
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