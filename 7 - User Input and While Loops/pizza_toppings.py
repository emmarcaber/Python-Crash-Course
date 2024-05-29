prompt = "\nTell me a pizza topping, and I will add it to your pizza:"
prompt += "\n(Enter 'quit' to end the program.) "

while True:
	message = input(prompt)

	if message == 'quit':
		break
	
	print(f"\nAdding {message} to your pizza.")

print("\nFinish cooking your pizza.")