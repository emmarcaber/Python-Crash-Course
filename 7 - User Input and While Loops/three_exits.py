active = True

while active:
	age = int(input("\nEnter your age: "))

	if age < 3:
		print("The ticket is free.")
	elif age > 3 and age < 12:
		print("The ticket is $10.")
	elif age > 100:
		active = False
	elif age <= 0:
		break
	else:
		print("The ticket is $15.")