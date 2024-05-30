def create_sandwich(*fillings):
	"""Show the filling of sandwich."""
	print("\nFilling of sandwich:")
	for filling in fillings:
		print(f"- {filling}")

	print("Your sandwich is finished!")

create_sandwich("tomato", "ham", "mayonnaise")
create_sandwich("cucumber", "banana", "egg")
create_sandwich("ham", "cheese")