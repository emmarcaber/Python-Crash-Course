print("Give me two numbers, and I'll add them.")
first_number = input("\nEnter first number: ")
second_number = input("Enter second number: ")

try:
	total = int(first_number) + int(second_number)
except ValueError:
	print("You cannot add a character to a number!")
else:
	print(total)