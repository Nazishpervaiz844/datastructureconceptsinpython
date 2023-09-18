# DICTIONARY

# clear() Removes all the elements from the dictionary
phone =	{
  "brand": "Google",
  "model": "Pixel 5",
  "year": 2020
}
print(phone)
phone.clear()
print("clear",phone)
print("---------------------------------------------------")

# copy() Returns a copy of the dictionary
phone =	{
  "brand": "Google",
  "model": "Pixel 5",
  "year": 2020
}
print(phone)
x = phone.copy()
print("copy",x)
print("---------------------------------------------------")

# fromkeys() Returns a dictionary with the specified keys and value
keys_list = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys_list)
print(new_dict)

keys_list = ['a', 'b', 'c']
y = 0 , 4
new_dict = dict.fromkeys(keys_list, y)
print(new_dict)
print("---------------------------------------------------")

# get() Returns the value of the specified key
phone =	{
  "brand": "Google",
  "model": "Pixel 5",
  "year": 2020
}
print(phone)
x = phone.get("model")
print(x)
print("---------------------------------------------------")

# items() Returns a list containing a tuple for each key value pair
phone =	{
  "brand": "Google",
  "model": "Pixel 5",
  "year": 2020
}
print(phone)
x = phone.items()
print(x)
print("---------------------------------------------------")

# keys() Returns a list containing the dictionary's keys
phone =	{
  "brand": "Google",
  "model": "Pixel 5",
  "year": 2020
}
x = phone.keys()
print(x)
print("---------------------------------------------------")

# pop() Removes the element with the specified key
phone =	{
  "brand": "Google",
  "model": "Pixel 5",
  "year": 2020
}
print(phone)
phone.pop("brand")
print("pop",phone)
print("---------------------------------------------------")

# popitem() Removes the last inserted key-value pair
phone =	{
  "brand": "Google",
  "model": "Pixel 5",
  "year": 2020
}
print(phone)
phone.popitem()
print("popitem",phone)
print("---------------------------------------------------")

# setdefault() Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
phone =	{
  "brand": "Google",
  "model": "Pixel 5",
  "year": 2020
}
print(phone)
x = phone.setdefault("brand","Samsung")
print("set_default",x)
print("---------------------------------------------------")

# update() Updates the dictionary with the specified key-value pairs
phone =	{
  "brand": "Google",
  "model": "Pixel 5",
  "year": 2020
}
print(phone)
phone.update({"ram": "8gb"})
print(phone)
print("---------------------------------------------------")

# values() Returns a list of all the values in the dictionary
phone =	{
  "brand": "Google",
  "model": "Pixel 5",
  "year": 2020
}
print(phone)
x = phone.values()
print(x)
print("---------------------------------------------------")