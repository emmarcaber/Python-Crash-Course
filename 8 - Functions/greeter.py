# def greet_user(username):
# 	"""Display a simple greeting."""
# 	print(f"Hello, {username.title()}!")

# greet_user("jesse")

def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	return f"{first_name} {last_name}".title()

while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")

	f_name = input("First Name: ")

	if f_name == 'q':
		break

	l_name = input("Last Name: ")
	
	if f_name == 'q':
		break

	print(f"Hello, {get_formatted_name(f_name, l_name)}!")