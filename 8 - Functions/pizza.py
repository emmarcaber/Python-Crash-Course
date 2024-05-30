# Passing an Arbitrary Arguments to a Function
# def make_pizza(*toppings):
# 	"""Summarize the pizza we are about to make."""
# 	print("\nMaking a pizza with the following toppings: ")
# 	for topping in toppings:
# 		print(f"- {topping}")

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make."""
	print(f"\nMaking a {size}-inch pizza with the following toppings: ")
	for topping in toppings:
		print(f"- {topping}")