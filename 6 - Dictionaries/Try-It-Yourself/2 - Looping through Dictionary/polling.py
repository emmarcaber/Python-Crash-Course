favorite_languages = {
	"jen": "python",
	"sarah": "c",
	"edward": "ruby",
	"phil": "python",
}

responders = [
	"jen",
	"emmar",
	"baracina",
	"angel",
	"bianca",
	"yasuo",
	"edward",
	"sarah",
	"phil"
]

for person in responders:
	if person not in favorite_languages.keys():
		print(f"{person.title()}, I invite you to answer the poll.")
	else:
		print(f"{person.title()}, thank you for responding to the poll.")
