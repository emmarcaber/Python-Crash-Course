team_members = [
	{
		"full_name": "emmar caber",
		"role": "fullstack engineer",
	},
	{
		"full_name": "jorel agustin",
		"role": "frontend engineer",
	},
	{
		"full_name": "ivan jefferson calleja",
		"role": "quality assurance tester",
	},
	{
		"full_name": "jake agnas",
		"role": "quality assurance tester",
	},
	{
		"full_name": "kian adrisola",
		"role": "project manager",
	},
	{
		"full_name": "zarina kate lagatic",
		"role": "project manager",
	},
]

for team_member in team_members:
	print(f"Name: {team_member['full_name'].title()}")
	print(f"Role: {team_member['role'].title()}\n")