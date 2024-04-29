# #add
# #update
# #explore set.etc sgle
# my_set={1,2,3,4,5,6,7,8}
# my_set.add(10)
# print(my_set)
# my_set.update()

# Using set()
my_set = set()

# Initializing with values
my_set = {1, 2, 3}

# Adding elements
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

my_set.update([5, 6])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Removing elements
my_set.remove(4)
print(my_set)  # Output: {1, 2, 3, 5, 6}

my_set.discard(5)
print(my_set)  # Output: {1, 2, 3, 6}

popped_element = my_set.pop()
print(popped_element)  # Output: 1
print(my_set)         # Output: {2, 3, 6}

