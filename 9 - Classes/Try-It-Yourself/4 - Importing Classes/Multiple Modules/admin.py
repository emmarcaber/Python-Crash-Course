from user import User
from privileges import Privileges

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