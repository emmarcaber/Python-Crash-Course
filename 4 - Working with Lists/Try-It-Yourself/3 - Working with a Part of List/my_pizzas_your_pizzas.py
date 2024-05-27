pizzas = ["Ham and Cheese", "Spicy", "Hawaiian"]
friend_pizzas = pizzas[:] # Create a copy

pizzas.append("Pepperoni")
friend_pizzas.append("Spaghetti")

print("My favorite pizzas are:")
for pizza in pizzas:
	print(f"- {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(f"- {pizza}")