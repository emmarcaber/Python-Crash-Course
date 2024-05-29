alien_0 = {"color": "green", "points": 5}
print(alien_0)

# Assign values to a dictionary key-value
# new_points = alien_0["points"]

# Add new key-value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with Empty Dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# Modifying Values in a Dictionary
alien_0 = {"color": "green"}
print(f"The alien is {alien_0['color']}.")

alien_0["color"] = "yellow"
print(f"The alien is now {alien_0['color']}.")

alien_0 = {
	"x_position": 0, 
	"y_position": 25, 
	"speed": "medium",
}
print(f"Original Position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == "slow":
	x_increment = 1
elif alien_0['speed'] == "medium":
	x_increment = 2
else:
	# This must be a fast alien.
	x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"New Position: {alien_0['x_position']}")

# Removing key-value pairs
alien_0 = {"color": "green", "points": 5}
print(alien_0)

del alien_0["points"]
print(alien_0)