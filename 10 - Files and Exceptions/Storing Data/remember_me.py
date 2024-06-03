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


def get_new_username():
	"""Prompt for a new username."""
	username = input("What is your name? ")

	filename = "username.json"
	with open(filename) as f:
		json.dump(username, f)
		print(f"We'll remember you when you come back, {username}!")


def greet_user():
	"""Greet the user by name."""
	username = get_stored_username()

	if username:
		print(f"Welcome back, {username}!")
	else:
		get_new_username()
	

greet_user()