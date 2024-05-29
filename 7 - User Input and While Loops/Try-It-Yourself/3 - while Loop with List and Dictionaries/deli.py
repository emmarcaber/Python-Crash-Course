sandwich_orders = [
	"spicy sandwich",
	"peanut butter sandwich",
	"mayonnaise sandwich",
	"tuna sandwich",
	"egg sandwich",
]
finished_sandwiches = []

while sandwich_orders:
	finished_sandwich = sandwich_orders.pop()
	print(f"I made your {finished_sandwich}.")
	finished_sandwiches.append(finished_sandwich)

print("\nFinished Sandwiches:")
for finished_sandwich in finished_sandwiches:
	print(f"\t{finished_sandwich.title()}")
