def read_content_of_file(filename):
	"""Read the content of a file."""

	try:
		with open(filename) as file_object:
			contents = file_object.read()
			print(contents.rstrip())
	except FileNotFoundError:
		pass


filenames = ["cats.txt", "dogs.txt", "hello.txt"]
for filename in filenames:
	read_content_of_file(filename)