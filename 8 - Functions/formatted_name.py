# Make an argument optional
def get_formatted_name(first_name, last_name, middle_name=''):
	"""Return a full name, neatly formatted."""
	if middle_name:
		full_name =  f"{first_name} {middle_name} {last_name}".title()
	else:
		full_name =  f"{first_name} {last_name}".title()

	return full_name


musician = get_formatted_name("jimi", "hendrix")
print(musician)

musician = get_formatted_name("john", "hooker", "lee")
print(musician)