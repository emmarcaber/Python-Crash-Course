my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:] # Copy a list

my_foods.append("cannoli")
friend_foods.append("ice cream")

for food in my_foods:
	print(food)

print()
for food in friend_foods:
	print(food)