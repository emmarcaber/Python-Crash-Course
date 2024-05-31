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


def determine_if_winner(winning_combination):
	"""Return true if my ticket already won."""
	my_ticket = [2, 4, 6, 8]

	# Loop to determine if I won
	for ticket_item, winning_combination_item in zip(my_ticket, winning_combination):
		if ticket_item != winning_combination_item:
			return False

	return True


count = 0
while True:
	winning_combination = get_winning_combination()
	result = determine_if_winner(winning_combination)

	if result:
		print(*winning_combination)
		break
	else:
		count += 1

print(f"Total Trials to Win: {count}")