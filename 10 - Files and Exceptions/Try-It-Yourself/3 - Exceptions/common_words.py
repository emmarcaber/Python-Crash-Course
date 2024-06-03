def count_words_from_file(filename, common_word):
	"""Count the common words from a file."""
	try:
		with open(filename, encoding="UTF-8") as f:
			content = f.readlines()
	except:
		print("File not found!")
	else:
		total_word_count = 0
		for line in content:
			total_word_count += line.lower().count(common_word)
		print(total_word_count)


count_words_from_file("laws_of_power.txt", "the ")
count_words_from_file("laws_of_power.txt", "the")
count_words_from_file("laws_of_power.txt", "then")
count_words_from_file("laws_of_power.txt", "there")