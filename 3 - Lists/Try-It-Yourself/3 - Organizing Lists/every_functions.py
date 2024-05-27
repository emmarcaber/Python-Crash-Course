mountains = ["Everest", "Mayon", "Banahaw", "Bulusan"]
rivers = ["Waras", "Amazon", "Nile"]
cities = ["Iriga", "Naga", "Legazpi", "Pili"]

# Adding Elements
mountains.append("Olympus Mons")
print(mountains)
rivers.insert(0, "Buhi")
print(rivers)

# Remove Elements
removed_cities = cities.pop()
print(removed_cities)
print(cities)

del cities[0]
print(cities)

remove_naga = "Naga"
cities.remove(remove_naga)
print(cities)

# Update Elements
cities[-1] = "Iriga"
print(cities) 

# Organizing Elements
places_to_visit = ["Ilocos Sur", "Paris", "Iceland", "Japan", "Germany"]

# Sorting without updating the original list
print(places_to_visit)
print(sorted(places_to_visit))
print(places_to_visit)
print(sorted(places_to_visit, reverse=True))

# Reverse the original list
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.reverse()

# Sort affecting the original list
places_to_visit.sort()
print(places_to_visit)
places_to_visit.sort(reverse=True)
print(places_to_visit)