class User:
	"""Create a User class."""

	def __init__(self, first_name, last_name, username):
		self.first_name = first_name
		self.last_name = last_name
		self.username = username


	def get_full_name(self):
		return f"{self.first_name} {self.last_name}".title()


	def describe_user(self):
		"""Display the user information."""
		print(f"\nUser Information:")
		print(f" - Name: {self.get_full_name()}")
		print(f" - Username: {self.username}")


	def greet_user(self):
		"""Greet the current user."""
		print(f"Hello, {self.get_full_name()}!") 