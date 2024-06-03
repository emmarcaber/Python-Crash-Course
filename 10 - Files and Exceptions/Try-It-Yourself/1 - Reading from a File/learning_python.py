file_name = "learning_python.txt"

# Reading an Entire File
with open(file_name) as file_object:
	contents = file_object.read()
	print(contents.rstrip())

# Read a File by Looping over the Object
print()
with open(file_name) as file_object:
	for line in file_object:
		print(line.rstrip())

# Storing the Lines in list
with open(file_name) as file_object:
	lines = file_object.readlines()

print()
for line in lines:
	print(line.rstrip()) 