# Create an empty list and add the following elements about your location, in this order:
# - City
# - State or Province
# - A list with the temperatures the last three days
# - Your favorite animal

my_list = []
my_list.append("NYC")
my_list.append("NY")
my_list.append([80, 90, 100])
my_list.append("Eagle")
print(my_list)
# Then, remove the State, without using the indexes.
my_list.remove(my_list[1])
print(my_list)
# Bonus: Remove the last element, using a negative index.
del my_list[-1]
print(my_list)

