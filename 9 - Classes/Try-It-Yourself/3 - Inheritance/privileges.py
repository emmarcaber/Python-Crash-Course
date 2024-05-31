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


class Privileges:
	"""A simple representation to show the Privileges of a User."""

	def __init__(self):
		"""Initialize the privileges attribute."""
		self.privileges = ["can add post", "delete post", "can ban user"]


class Admin(User):
	"""A simple representation of Admin of a site."""

	def __init__(self, first_name, last_name, username):
		super().__init__(first_name, last_name, username)
		self.admin_privileges = Privileges()


	def show_privileges(self):
		"""Display the admin privileges."""
		print(f"{self.get_full_name()}, you have these privileges: ")
		for privilege_count, privilege in enumerate(self.admin_privileges.privileges):
			print(f"Privilege #{privilege_count + 1}: {privilege.title()}")

admin = Admin("Emmar", "Caber", "embre")
admin.greet_user()
admin.show_privileges()