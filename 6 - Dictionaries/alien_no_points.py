# Using get() to Access Values
alien_0 = {
	"color": "green", 
	"speed": "slow",
}

# Results to error since there is no 
# key points in the alien_0 dictionary
# print(alien_0["points"])

# Better Approach
# Use get() method to assign argument which
# returns a value when a key does not exist
point_value = alien_0.get("points", "No point value assigned.")
print(point_value)