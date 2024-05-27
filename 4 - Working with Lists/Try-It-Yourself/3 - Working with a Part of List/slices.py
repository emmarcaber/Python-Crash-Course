foods = [
	"pizza", 
	"hotdog", 
	"hamburger", 
	"milktea", 
	"french fries",
	"spaghetti"
]

# Printing the first three items
print(foods[:3])

# Printing the middle three items
# Get the middle item by floor division
middle_item = len(foods) // 2

# Reduce by 1 since len() returns total count
# but index starts at 0
print(foods[middle_item - 1: middle_item + 2])

# Printing the last three items
print(foods[-3:])