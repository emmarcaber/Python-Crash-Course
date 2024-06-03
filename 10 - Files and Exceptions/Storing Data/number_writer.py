# Using json.dump() and json.load()
import json

numbers = [2, 3, 5, 7, 13]

filename = "numbers.json"
with open(filename, "w") as f:
	json.dump(numbers, f)