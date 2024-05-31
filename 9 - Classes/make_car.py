# Importing a Single Class
from car import Car

my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying an Attribute's Value Directly
my_new_car.odomoter_reading = 23
my_new_car.read_odometer()

# Modifying an Attribute's Value Through a Method
my_new_car.update_odometer(25)
my_new_car.read_odometer()

# Reject the update of odometer
# Since it is lower than the old odometer
my_new_car.update_odometer(23)

# Increment odometer
my_new_car.increment_odometer(23_500)
my_new_car.read_odometer()

my_new_car.increment_odometer(200)
my_new_car.read_odometer()