# Create the list that will contain the responses.
responses = {}

# Flag to exit the loop.
active = True

while active:
	# Ask for name and response.
	name = input("\nWhat is your name? ")
	response = input("If you could visit one place in the world, where would you go? ")

	# Add the name and response to dictionary
	responses[name] = response

	# Prompt the user if another person wants to continue.
	do_repeat = input("Do you want another person to still answer? (yes/no) ")
	if do_repeat.lower() == "no":
		active = False

# Showing the poll results.
print("\n--- Poll Results --- ")
for name, response in responses.items():
	print(f"{name.title()} would like to visit {response}.")