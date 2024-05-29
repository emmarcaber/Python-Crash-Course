rivers = {
	"nile": "egypt",
	"amazon": "brazil",
	"pasig": "philippines",
}

for river, country in rivers.items():
	print(f"{river.title()} runs through {country.title()}.")