# Dictionary of Similar Objects
favorite_languages = {
	"jen": "python",
	"sarah": "c",
	"edward": "ruby",
	"phil": "python",
}


# Brute-force Approach
# language = favorite_languages["sarah"].title()
# print(f"Sarah's favorite language is {language}.")


# Better Approach
# for person, language in favorite_languages.items():
# 	print(f"{person.title()}'s favorite language is {language.title()}.")


# Get the name of persons with keys()
# for name in favorite_languages.keys():
# 	print(f"{name.title()}")


# Looping through all the Keys in a Dictionary
# friends = ["phil", "sarah"]
# for name in favorite_languages.keys():
# 	print(f"{name.title()}")

# 	if name in friends:
# 		language = favorite_languages[name].title()
# 		print(f"\t{name.title()}, I see you love {language}!")


# Use if Condition if a string is in dictionary keys()
# if "erin" not in favorite_languages.keys():
# 	print("Erin, please take our poll!")


# Looping through a Dictionary's Keys 
# in a Particular Order
# for name in sorted(favorite_languages.keys()):
# 	print(f"{name.title()}, thank you for taking the poll.")


# Looping through all Values in a Dictionary
# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
# 	print(language.title())

favorite_languages = {
	"jen": ["python", "ruby"],
	"sarah": ["c"],
	"edward": ["ruby", "go"],
	"phil": ["python", "haskell"],
}

for name, languages in favorite_languages.items():
	if len(languages) == 1:
		print(f"\n{name.title()}'s favorite language is {languages[0].title()}.")
	else:
		print(f"\n{name.title()}'s favorite languages are: ")
		for language in languages:
			print(f"\t{language.title()}")