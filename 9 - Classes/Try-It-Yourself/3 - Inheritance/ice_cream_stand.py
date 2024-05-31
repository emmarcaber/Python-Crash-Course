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


class IceCreamStand(Restaurant):
	"""A simple representation about an Ice Cream stand."""

	def __init__(self, restaurant_name, cuisine_type):
		"""
		Initialize the attributes of superclass.
		Add flavors attribute.
		"""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ["strawberry", "ube", "double dutch"]


	def display_flavors(self):
		"""Display the ice cream stand flavors."""
		print("\nShowing all the flavors:")
		for count, flavor in enumerate(self.flavors):
			print(f"Flavor #{count + 1}: {flavor.title()}")


abec = IceCreamStand("abec", "philippine")
abec.describe_restaurant()
abec.open_restaurant()
abec.display_flavors()