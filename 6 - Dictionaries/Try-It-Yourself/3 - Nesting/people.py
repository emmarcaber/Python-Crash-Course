people = {
	"angel":{
		"first_name": "angel bianca",
		"last_name": "nacario",
		"age": 22,
	},
	"emmar":{
		"first_name": "emmar",
		"last_name": "caber",
		"age": 21,
	},
}

for username, user_info in people.items():
	print(f"Username: {username}")
	full_name = f"{user_info['first_name']} {user_info['last_name']}".title()
	print(f"Full Name: {full_name}")
	print(f"Age: {user_info['age']}\n")	