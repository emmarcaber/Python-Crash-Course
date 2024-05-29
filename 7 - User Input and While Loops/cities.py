prompt = "\nPlease enter the name of a city you have visited."
prompt += "\n(Enter the 'quit' when you are finished.) "

while True:
	city = input(prompt)

	if city == "quit":
		break
	else:
		print(f"I'd love to go {city.title()}!")