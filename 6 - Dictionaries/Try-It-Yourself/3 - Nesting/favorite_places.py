favorite_places = {
	"angel": [
		"japan",
		'germany',
		'cambodia'
	],
	"emmar": [
		"camarines sur",
		'pangasinan',
		'japan'
	],
	"matet": [
		"iceland",
		'france',
		'spain'
	],
}

for person, favorite_places in favorite_places.items():
	print(f"\n{person.title()}' favorite places are: ")

	for favorite_place in favorite_places:
		print("\t" + favorite_place.title())

