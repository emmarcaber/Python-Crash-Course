cities = {
	"iriga": {
		"country": "Philippines",
		"population": 50_000,
		"fact": "hometown",
	},
	"naga": {
		"country": "Philippines",
		"population": 80_000,
		"fact": "First SM in Bicol",
	},
	"legazpi": {
		"country": "Philippines",
		"population": 100_000,
		"fact": "SM Legazpi",
	},
}

for city, city_info in cities.items():
	print(f"\n{city.title()} City's Information: ")

	for info, value in city_info.items():
		print(f"\t{info.title()}: {value}")