from random import randint

class Die:
	"""A simple representation of a die."""

	def __init__(self, size=6):
		"""Initialize the attributes."""
		self.size = size

	def roll_die(self):
		"""Roll the die in accorandance with its size."""
		print(randint(1, self.size))


def show_result_statement(size):
	"""Print a intro statement to show the roll results."""
	print(f"\n{size}-sided Die Roll Results: ")


# 6-sided die instance
die_6 = Die()
show_result_statement(die_6.size)
die_6.roll_die()
die_6.roll_die()
die_6.roll_die()
die_6.roll_die()
die_6.roll_die()
die_6.roll_die()
die_6.roll_die()
die_6.roll_die()
die_6.roll_die()
die_6.roll_die()

# 10-sided die instance
die_10 = Die(10)
show_result_statement(die_10.size)
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()

# 20-sided die instance
die_20 = Die(20)
show_result_statement(die_20.size)
die_20.roll_die()
die_20.roll_die()
die_20.roll_die()
die_20.roll_die()
die_20.roll_die()
die_20.roll_die()
die_20.roll_die()
die_20.roll_die()
die_20.roll_die()
die_20.roll_die()