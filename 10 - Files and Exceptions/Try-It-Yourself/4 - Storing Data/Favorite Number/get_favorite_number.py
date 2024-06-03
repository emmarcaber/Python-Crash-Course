import json

filename = "favorite_number.txt"
with open(filename) as f:
	favorite_number = json.load(f)
	print(f"I know your favorite number! It's {favorite_number}!")