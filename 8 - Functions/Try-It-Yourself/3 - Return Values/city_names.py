def get_formatted_city_country(city, country):
	"""Get formatted city and country."""
	return f"{city}, {country}".title()

print(get_formatted_city_country("iriga", "philippines"))
print(get_formatted_city_country("santiago", "chile"))
print(get_formatted_city_country("new york", "USA"))
