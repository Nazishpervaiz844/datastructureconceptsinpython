# tupes

# 1	cmp(tuple1, tuple2)	It compares two tuples and returns true if tuple1 is greater than tuple2 otherwise false.
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
if tuple1 > tuple2:
    print("tuple1 is greater than tuple2")
elif tuple1 < tuple2:
    print("tuple1 is less than tuple2")
else:
    print("tuple1 and tuple2 are equal")
print("---------------------------------------------------")

# 2	len(tuple)	It calculates the length of the tuple.
tuple1 = (1, 2, 3, 4, 5)
length_of_tuple = len(tuple1)
print("The length of the tuple is:", length_of_tuple)
print("---------------------------------------------------")

# 3	max(tuple)	It returns the maximum element of the tuple
tuple1 = (1, 2, 3, 4, 5,9)
max_element = max(tuple1)
print("The maximum element of the tuple is:", max_element)
print("---------------------------------------------------")

# 4	min(tuple)	It returns the minimum element of the tuple.
tuple1 = (1, 2, 3, 4, 5,9)
max_element = min(tuple1)
print("The maximum element of the tuple is:", max_element)
print("---------------------------------------------------")

# 5	tuple(seq)	It converts the specified sequence to the tuple.
list1 = ['maths', 'che', 'phy', 'bio']
tuple1 = tuple(list1)
print ("tuple elements : ", tuple1)
print("---------------------------------------------------")