import json

def get_stored_favorite_number():
	"""Get stored favorite number if available."""
	filename = 'favorite_number.json'
	try:
		with open(filename) as f:
			favorite_number = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return favorite_number


def get_new_favorite_number():
	"""Prompt for a new favorite number."""
	favorite_number = input("What is your favorite number? ")

	filename = "favorite_number.json"
	with open(filename, "w") as f:
		json.dump(favorite_number, f)
		print(f"We'll remember your favorite number which is {favorite_number}!")


def show_favorite_number():
	"""Show the favorite number."""
	favorite_number = get_stored_favorite_number()

	if favorite_number:
		print(f"I know your favorite number, it's {favorite_number}!")
	else:
		get_new_favorite_number()
	

show_favorite_number()