def make_album(artist_name, artist_title, number_of_songs=0):
	"""Make an album"""
	album = {
		"artist_name": artist_name,
		"artist_title": artist_title
	}

	if number_of_songs:
		album["number_of_songs"] = number_of_songs

	return album

print(make_album("embre", "singerist"))
print(make_album("abenaca", "singerisa", 3))
print(make_album("emary", "writer", 10))
