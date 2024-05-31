class Restaurant:
	"""Create a class Restaurant."""

	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize the restaurant_name and cuisine_type attributes"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type


	def describe_restaurant(self):
		"""Describe the restaurant."""
		print(f"Welcome to {self.restaurant_name.title()}, a {self.cuisine_type.title()} cuisine specialist!")


	def open_restaurant(self):
		"""Open the restaurant."""
		print(f"{self.restaurant_name.title()} is now open.")