motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

# modify first element
motorcycles[0] = "ducati"
print(motorcycles)

motorcycles.append("ducati")
print(motorcycles)

motorcycles = []

# add elements
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")

print(motorcycles)

# insert elements
motorcycles.insert(0, "ducati")
print(motorcycles)

# Remove an Item using del statement
del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# Remove the last item using pop() method
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# Popping items from any position list
# Use the index of item to remove 
# as an argument of the pop() method
motorcycles = ["honda", "yamaha", "suzuki"]
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Removing an item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

# Remove the element with a value of "ducati"
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")