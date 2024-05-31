class User:
	"""Create a User class."""

	def __init__(self, first_name, last_name, username):
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.login_attempts = 0


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


	def increment_login_attempts(self):
		"""Increment login attempts by 1."""
		self.login_attempts += 1


	def reset_login_attempts(self):
		"""Reset the login attempts to 0."""
		print("\nResetting login attempts...")
		self.login_attempts = 0

	def show_total_login_attempts(self):
		"""Show the total login attempts."""
		print(f"Login Attempts: {self.login_attempts}")


user_0 = User("emmar", "caber", "embre")
user_0.increment_login_attempts()
user_0.show_total_login_attempts()

user_0.increment_login_attempts()
user_0.show_total_login_attempts()

user_0.increment_login_attempts()
user_0.show_total_login_attempts()

user_0.reset_login_attempts()
user_0.show_total_login_attempts()