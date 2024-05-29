current_users = ["emmar", "jorel", "angel", "ivan", "kian", "jake"]
new_users = ["kian", "jorel", "wanwan", "juan", "carlo"]

for new_user in new_users:
	if new_user.lower() in current_users:
		print(f"Sorry {new_user}, you need to enter a new username.")
	else:
		print(f"{new_user}, your username is available.")