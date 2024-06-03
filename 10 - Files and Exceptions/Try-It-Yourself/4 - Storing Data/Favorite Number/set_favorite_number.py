import json

favorite_number = input("What is your favorite number? ")
filename = "favorite_number.txt"
with open(filename, "w") as f:
	json.dump(favorite_number, f)
	print("I'll remember your favorite number.")