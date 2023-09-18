#LIST

# append() Adds an element at the end of the list

city = ['KARACHI', 'LAHORE', 'PESHAWAR']
city.append('ISLAMABAD')
print(city)
print("---------------------------------------------------")
# clear()	Removes all the elements from the list
city = ['KARACHI', 'LAHORE', 'PESHAWAR']
city.clear()
print(city)
print("---------------------------------------------------")

# copy() Returns a copy of the list
city = ['KARACHI', 'LAHORE', 'PESHAWAR']
x = city.copy()
print(x)
print("---------------------------------------------------")

# count()	Returns the number of elements with the specified value
city = ['KARACHI', 'LAHORE', 'PESHAWAR', 'KARACHI']
X = city.count('KARACHI')
print(X)
print("---------------------------------------------------")

# extend() Add the elements of a list (or any iterable), to the end of the current list
city = ['KARACHI', 'LAHORE', 'PESHAWAR', 'KARACHI']
country = ['PAKISTAN', 'USA', 'UAE']
city.extend(country)
print(city)
print("---------------------------------------------------")

# index() Returns the index of the first element with the specified value
city = ['KARACHI', 'LAHORE', 'PESHAWAR']
x = city.index('PESHAWAR')
print(x)
print("---------------------------------------------------")

# insert() Adds an element at the specified position
city = ['KARACHI', 'LAHORE', 'PESHAWAR']
city.insert(2, 'ISLAMABAD')
print(city)
print("---------------------------------------------------")
# pop() Removes the element at the specified position
city = ['KARACHI', 'LAHORE', 'PESHAWAR']
city.pop(2)
print(city)
print("---------------------------------------------------")

# remove() Removes the first item with the specified value
city = ['KARACHI', 'LAHORE', 'PESHAWAR', 'ISLAMABAD']
city.remove("LAHORE")
print(city)
print("---------------------------------------------------")

# reverse() Reverses the order of the list
city = ['KARACHI', 'LAHORE', 'PESHAWAR', 'ISLAMABAD']
city.reverse()
print(city)
print("---------------------------------------------------")


# sort() Sorts the list
city = ['KARACHI','ABBOTABAD', 'LAHORE', 'PESHAWAR', 'ISLAMABAD']
city.sort()
print(city)
print("---------------------------------------------------")




