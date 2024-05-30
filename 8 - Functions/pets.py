def describe_pet(pet_name,animal_type="dog"):
	"""Display information about a pet."""
	print(f"\nI have a {animal_type}.")
	print(f"My animal {animal_type}'s name is {pet_name.title()}.")

# Positional Arguments
# describe_pet("hamster", "harry")
# describe_pet("dog", "willie")

# Keyword Arguments
describe_pet(animal_type="cat",pet_name="ming yao")
describe_pet(pet_name="dogie")