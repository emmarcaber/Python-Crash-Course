sandwich_orders = [
	"spicy sandwich",
	"peanut butter sandwich",
	"mayonnaise sandwich",
	"pastrami",
	"tuna sandwich",
	"pastrami",
	"egg sandwich",
	"pastrami",
]
finished_sandwiches = []

print("Deli has run out of pastrami.")

while sandwich_orders:
	finished_sandwich = sandwich_orders.pop()

	if finished_sandwich == "pastrami":
		print("We run out of pastrami. Pastrami is not made.")
		continue

	print(f"I made your {finished_sandwich}.")
	finished_sandwiches.append(finished_sandwich)

print("\nFinished Sandwiches:")
for finished_sandwich in finished_sandwiches:
	print(f"\t{finished_sandwich.title()}")