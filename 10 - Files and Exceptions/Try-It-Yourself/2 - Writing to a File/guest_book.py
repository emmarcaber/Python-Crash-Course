filename = "guest_book.txt"

while True:
	prompt = "\nEnter your name: "
	prompt += "\n(enter 'q' to quit.) "
	name = input(prompt)

	if name == "q":
		break

	# Greet the user
	# Then, add it to the file.
	print(f"Hello, {name}!")
	with open(filename, "a") as file_object:
		file_object.write(f"{name}\n")
