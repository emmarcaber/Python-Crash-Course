# Part 1 - Multiple Conditions
# requested_toppings = ["mushrooms", "extra cheese"]

# if "mushrooms" in requested_toppings:
# 	print("Adding mushrooms.")
# if "pepperoni" in requested_toppings:
# 	print("Adding pepperoni.")
# if "extra cheese" in requested_toppings:
# 	print("Adding extra cheese.")

# print("\nFinished making your pizza!")

# Part 2 - if Statements inside loops
# requested_toppings = ["mushroooms", "green peppers", "extra cheese"]

# for request_topping in requested_toppings:
# 	if request_topping == 'green peppers':
# 		print("Sorry, we are out of green peppers right now.")
# 	else:
# 		print(f"Adding {request_topping}.")

# print("\nFinished making your pizza!")

# requested_toppings = []

# if requested_toppings:
# 	for request_topping in requested_toppings:
# 		print(f"Adding {request_topping}!")

# 	print("\nFinisshed making your pizza!")
# else:
# 	print("Are you sure you want a plain pizza?")

# Part 3 - Using Multiple Lists
available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!") 