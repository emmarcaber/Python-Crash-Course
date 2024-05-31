from random import choice

def get_winning_combination():
	"""Return a list of winning combination."""
	digits_letters = [
		*list(range(0,10)),
		'A',
		'B',
		'C',
		'D',
		'E'
	]

	# A list to store winning combination
	winning_combination = []

	# Get the four letter or number combination
	for dl in range(4):
		winning_combination.append(choice(digits_letters))

	return winning_combination


print("Any ticket matching these four number or letters wins a prize:")
print(*get_winning_combination())