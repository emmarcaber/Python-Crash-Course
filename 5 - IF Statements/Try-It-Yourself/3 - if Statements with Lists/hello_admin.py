usernames = ["emmar", "baracina", "caber", "admin", "angel", "bianca", "erlano", "nacario"]

# for user in usernames:
# 	if user.lower() == "admin":
# 		print(f"Hello {user}, would like to see a status report?")
# 	else:
# 	

# usernames = []

if usernames:
	for user in usernames:
		if user.lower() == "admin":
			print(f"Hello {user}, would like to see a status report?")
		else:
			print(f"Hello {user.title()}, thank you for logging in again.")
else:
	print("We need to find some users!")