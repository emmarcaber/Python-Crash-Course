dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# changing an element from tuple will result to error
# ypeError: 'tuple' object does not support item assignment
# dimensions[0] = 250

# Writing over a tuple
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)


dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)