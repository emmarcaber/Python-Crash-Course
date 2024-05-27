players  = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3]) # ["charles", "martina", "michael"]

print(players[1:4]) # ['martina', 'michael', 'florence']

# Without a starting index, Python starts at 
# the beginning of the list
print(players[:4]) #  ['charles', 'martina', 'michael', 'florence']

# Without a stopping index, Python stops at 
# the end of the list
print(players[2:]) # ['michael', 'florence', 'eli']

# Output the last three players
# Since it starts at the third last player
print(players[-3:])

# Note
# You can include a third value in the brackets indicating a slice. If a third
# value is included, this tells Python how many items to skip between items
# in the specified range.

# Alternative reverse, instead of reverse() method
# and sorted(reverse=True)
print(players[1::2])

players = ["charles", "martina", "michael", "florence", "eli"]

print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())