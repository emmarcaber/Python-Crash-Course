pet_0 = {"name": "dogie", "owner": "emman", "type": "dog"}
pet_1 = {"name": "ming yao", "owner": "emmar", "type": "cat"}
pet_2 = {"name": "dojie", "owner": "matet", "type": "dog"}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
	print(f"Name: {pet['name'].title()}")
	print(f"Owner: {pet['owner'].title()}")
	print(f"Type of Animal: {pet['type'].title()}\n")