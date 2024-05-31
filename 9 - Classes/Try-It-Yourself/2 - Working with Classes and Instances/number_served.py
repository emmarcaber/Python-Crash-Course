class Restaurant:
	"""Create a class Restaurant."""

	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize the restaurant_name and cuisine_type attributes"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Describe the restaurant."""
		print(f"Welcome to {self.restaurant_name.title()}, a {self.cuisine_type.title()} cuisine specialist!")

	def open_restaurant(self):
		"""Open the restaurant."""
		print(f"{self.restaurant_name.title()} is now open.")

	def show_number_served(self):
		"""Show the total number served by the restaurant."""
		print(f"{self.restaurant_name.title()} has served {self.number_served} table(s).")

	def set_number_served(self, served):
		"""Set the number served."""
		self.number_served = served

	def increment_number_served(self, served):
		"""Increment the number served."""
		self.number_served += served



restaurant = Restaurant("itadaki", "japan")
restaurant.show_number_served()

restaurant.set_number_served(21)
restaurant.show_number_served()

restaurant.increment_number_served(25)
restaurant.show_number_served()