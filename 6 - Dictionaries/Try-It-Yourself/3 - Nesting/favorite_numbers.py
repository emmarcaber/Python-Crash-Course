favorite_numbers = {
	"emmar": [8, 25],
	"emary": [30, 3],
	"matet": [24, 28],
	"emman": [28, 21],
}

for person, favorite_numbers in favorite_numbers.items():
	print(f"\n{person.title()}' favorite numbers are: ")

	for number in favorite_numbers:
		print(f"\t{number}")