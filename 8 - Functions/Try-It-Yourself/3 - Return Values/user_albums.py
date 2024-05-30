def make_album(artist_name, artist_title):
	"""Make an album that returns dictionary."""
	return {"artist_name": artist_name, "artist_title": artist_title}

while True:
	print("\nEnter an album:")
	print("(enter 'q' to quit)")

	a_name = input("Enter the artist name: ")

	if a_name == 'q':
		break

	a_title = input("Enter the artist title: ")

	if a_title == 'q':
		break

	print(make_album(a_name, a_title))