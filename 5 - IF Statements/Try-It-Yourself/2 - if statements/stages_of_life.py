def determine_stage_of_life(age):
	if age < 2:
		stage_of_life = "baby"
	elif age > 2 and age < 4:
		stage_of_life = "toddler"
	elif age > 4 and age < 13:
		stage_of_life = "kid"
	elif age > 13 and age < 20:
		stage_of_life = "teenager"
	elif age > 20 and age < 65:
		stage_of_life = "adult"
	elif age > 65:
		stage_of_life = "elder"

	print(f"Person is a {stage_of_life}.")

determine_stage_of_life(1)
determine_stage_of_life(3)
determine_stage_of_life(6)
determine_stage_of_life(14)
determine_stage_of_life(22)
determine_stage_of_life(81)