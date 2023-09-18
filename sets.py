# SETS

# add() Adds an element to the set
colors = {"yellow", "red", "blue"}
print(colors)
colors.add("green")
print(colors)
print("---------------------------------------------------")

# clear() Removes all the elements from the set
colors = {"yellow", "red", "blue"}
print(colors)
colors.clear()
print(colors)
print("---------------------------------------------------")

# copy() Returns a copy of the set
colors = {"yellow", "red", "blue"}
x = colors.copy()
print(x)
print("---------------------------------------------------")

# difference() Returns a set containing the difference between two or more sets
colors = {"yellow", "red", "orange", "green"}
city = {"karachi", "lahore", "islamabad", "yellow"}
z = colors.difference(city)
print(z)
print("---------------------------------------------------")

# difference_update() Removes the items in this set that are also included in another, specified set
colors = {"yellow", "red", "orange", "green", "purple"}
city = {"karachi", "lahore", "islamabad", "green"}
colors.difference_update(city)
print(colors)
print("---------------------------------------------------")

# discard() Remove the specified item
colors = {"yellow", "red", "orange", "green", "purple"}
print(colors)
colors.discard("orange")
print(colors)
print("---------------------------------------------------")

# intersection() Returns a set, that is the intersection of two or more sets
colors = {"yellow", "red", "orange", "green"}
city = {"karachi", "lahore", "islamabad", "yellow"}
z = colors.intersection(city)
print(z)
print("---------------------------------------------------")

# intersection_update() Removes the items in this set that are not present in other, specified set(s)
colors = {"pink", "red", "orange", "green"}
city = {"karachi", "lahore", "islamabad", "pink"}
colors.intersection_update(city)
print(colors)
print("---------------------------------------------------")

# isdisjoint() Returns whether two sets have a intersection or not
colors = {"yellow", "red", "orange", "green"}
city = {"karachi", "lahore", "islamabad", "yellow"}
z = colors.isdisjoint(city)
print(z)
print("---------------------------------------------------")

# issubset() Returns whether another set contains this set or not
colors = {"yellow", "red", "orange", "green"}
city = {"karachi", "lahore", "islamabad", "yellow", "red", "orange", "green"}
print(colors)
z = colors.issubset(city)
print(z)
print("---------------------------------------------------")

# issuperset() Returns whether this set contains another set or not
colors = {"yellow", "red", "orange", "green", "karachi", "lahore", "islamabad"}
city = {"karachi", "lahore", "islamabad"}
print(colors)
z = colors.issuperset(city)
print(z)
print("---------------------------------------------------")

# pop() Removes an element from the set
colors = {"yellow", "red", "blue"}
print(colors)
colors.pop()
print(colors)
print("---------------------------------------------------")

# remove() Removes the specified element
colors = {"yellow", "red", "blue", "green"}
print(colors)
colors.remove("green")
print(colors)
print("---------------------------------------------------")

# symmetric_difference() Returns a set with the symmetric differences of two sets
colors = {"yellow", "red", "orange", "green"}
city = {"karachi", "lahore", "islamabad", "yellow"}
z = colors.symmetric_difference(city)
print(z)
print("---------------------------------------------------")

# symmetric_difference_update() Inserts the symmetric differences from this set and another
colors = {"yellow", "red", "orange", "green"}
city = {"karachi", "lahore", "islamabad", "yellow"}
colors.symmetric_difference(city)
print(colors)
print("---------------------------------------------------")

# union() Return a set containing the union of sets
colors = {"yellow", "red", "orange", "green"}
city = {"karachi", "lahore", "islamabad", "yellow"}
z = colors.union(city)
print(z)
print("---------------------------------------------------")

# update() Update the set with another set, or any other iterable
colors = {"yellow", "red", "orange", "green"}
city = {"karachi", "lahore", "islamabad", "yellow", "peshawar"}
colors.update(city)
print(colors)
print("---------------------------------------------------")
