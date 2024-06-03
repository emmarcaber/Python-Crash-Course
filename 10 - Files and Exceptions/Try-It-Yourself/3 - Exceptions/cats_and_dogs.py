def read_content_of_file(filename):
	"""Read the content of a file."""

	try:
		with open(filename) as file_object:
			contents = file_object.read()
			print(contents.rstrip())
	except FileNotFoundError:
		print("File not found!")


filenames = ["cats.txt", "dogs.txt", "hello.txt"]
for filename in filenames:
	read_content_of_file(filename)