import json

def get_stored_username():
	"""Get stored username if available."""
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username


def input_username():
	"""Prompt for name."""
	username = input("What is your name? ")
	return username


def get_new_username():
	"""Prompt for a new username."""
	username = input_username()

	filename = "username.json"
	with open(filename, "w") as f:
		json.dump(username, f)
		print(f"\nWe'll remember you when you come back, {username}!")


def verify_user(old_username):
	"""Verify if the current user is the old user."""
	if input_username() == old_username:
		print(f"\nWelcome back, {old_username}!")
	else: 
		print("\nIt seems you are not the old user.")
		print("Enter your name again.")
		get_new_username()


def greet_user():
	"""Greet the user by name."""
	old_username = get_stored_username()

	if old_username:
		verify_user(old_username)
	else:
		get_new_username()
	

greet_user()