# Better Approach
# Create a function
def determine_player_points(alien_color):
	if alien_color == "green":
		points = 5
	elif alien_color == "yellow":
		points = 10
	elif alien_color == "red":
		points = 15

	print(f"Player just earned {points} points.")

determine_player_points("green")
determine_player_points("yellow")
determine_player_points("red")