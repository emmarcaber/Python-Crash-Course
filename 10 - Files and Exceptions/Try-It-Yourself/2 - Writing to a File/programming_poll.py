filename = "responses.txt"

while True:
	prompt = "\nWhy do you love programming?"
	prompt += "\n(enter 'q' to quit.) "
	response = input(prompt)

	if response == "q":
		break

	# Print a message that the response was recorded.
	# Then, add it to the file.
	print(f"Response recorded.")
	with open(filename, "a") as file_object:
		file_object.write(f"{response}\n")
