def city_country(city, country, population=""):
	city_country = f"{city}, {country}".title()
	if population:
		city_country += f" - population {population}"
	return city_country