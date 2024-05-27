bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0]) # index starts at 0, access element of a list
print(bicycles[0].title()) # apply methods on a specific element
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1]) # get the last element automatically from the list

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)