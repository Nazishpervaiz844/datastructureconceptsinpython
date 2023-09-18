# STRINGS

#capitalize() Converts the first character to upper case
text = "pakistan zindabad"
print(text)
x = text.capitalize()  
print("capitalize", x)
print("---------------------------------------------------")

# casefold() Converts string into lower case
text = "PAKISTAN ZINDABAD"
print(text)
y = text.casefold()  
print("lower: ", y)
print("---------------------------------------------------")

# islower() Returns True if all characters in the string are lower case

text = "pakistan"
print(text)
x = text.islower()
print("is lower: ",x)
print("---------------------------------------------------")

# upper() Converts a string into upper case
text = "pakistan is a beautiful city"
print(text)
x = text.upper()
print("upper: ",x)
print("---------------------------------------------------")

# center() Returns a centered string
text = "pakistan"
print(text)
x = text.center(50)
print("center",x)
print("---------------------------------------------------")

# count() Returns the number of times a specified value occurs in a string
text = "PAKISTAN ZINDABAD. PAKISTAN IS A BEAUTIFUL CITY"
print(text)
y = text.count("PAKISTAN")  
print("count",y)
print("---------------------------------------------------")

# encode() Returns an encoded version of the string
text = "PAKISTâN ZINDABAD"
z = text.encode()  
print(z)
print("---------------------------------------------------")

# endswith() Returns true if the string ends with the specified value
text = "PAKISTAN ZINDABAD"
z = text.endswith(".")  
print(z)
print("---------------------------------------------------")


# expandtabs() Sets the tab size of the string   4 means 4 white spaces
text = "P\ta\tk\ti\ts\tt\ta\tn"
z = text.expandtabs(4)  
print(z)
print("---------------------------------------------------")

# find() Searches the string for a specified value and returns the position of where it was found
text = "PAKISTAN ZINDABAD. PAKISTAN IS A BEAUTIFUL CITY"
y = text.find("BEAUTIFUL")  
print(y)
print("---------------------------------------------------")
 
# format() Formats specified values in a string
#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "nazish", age = 23)
print(txt1)
print("---------------------------------------------------")

# format_map() Formats specified values in a string
a = {'x':'pakistan', 'y':'beautiful'}
print("{x} is {y}".format_map(a))
print("---------------------------------------------------")

# index() Searches the string for a specified value and returns the position of where it was found
text = "PAKISTAN ZINDABAD. PAKISTAN IS A BEAUTIFUL CITY"
x = text.index("CITY")
print("index",x)

# isalnum() Returns True if all characters in the string are alphanumeric
text = "Pakistan12"
x = text.isalnum()
print("is alphanumeric",x)

# isalpha() Returns True if all characters in the string are in the alphabet
text = "Pakistan12"
x = text.isalpha()
print("is alpha",x)

# isascii() Returns True if all characters in the string are ascii characters
text = "Pakistan12"
x = text.isascii()
print("is ascii",x)

# isdecimal() Returns True if all characters in the string are decimals
text = "123"
x = text.isdecimal()
print("is decimal",x)

# isdigit() Returns True if all characters in the string are digits
text = "pak123"
x = text.isdigit()
print("is digit",x)

# isidentifier() Returns True if the string is an identifier
text = "pakistanzindabad"
print(text)
x = text.isidentifier()
print("is identifier",x)
print("---------------------------------------------------")



# isnumeric() Returns True if all characters in the string are numeric
text = "12345"
print(text)
x = text.isnumeric()
print("is numeric: ", x)
print("---------------------------------------------------")

# isprintable() Returns True if all characters in the string are printable
text = "pakistan zindabad"
print(text)
x = text.isprintable()
print("is printable: ", x)
print("---------------------------------------------------")

# isspace() Returns True if all characters in the string are whitespaces
text = "pakistan zindabad"
print(text)
x = text.isspace()
print("is space: ", x)
print("---------------------------------------------------")

# istitle() Returns True if the string follows the rules of a title
text = "Pakistan Zindabad"
print(text)
x = text.istitle()
print("is title: ", x)
print("---------------------------------------------------")

# isupper() Returns True if all characters in the string are upper case
text = "pakistan zindabad"
print(text)
x = text.isupper()
print("is supper: ", x)
print("---------------------------------------------------")

# join() Converts the elements of an iterable into a string
text = ("pakistan","is", "beautiful", "city")
print(text)
x = "#".join(text)
print("is join: ",x)
print("---------------------------------------------------")

# ljust() Returns a left justified version of the string
text = "pakistan"
print(text)
x = text.ljust(20)
print(x, "is beautiful city.")
print("---------------------------------------------------")

# lower() Converts a string into lower case
text = "PAKISTAN ZINDABAD. PAKISTAN IS A BEAUTIFUL CITY"
print(text)
x = text.lower()
print("lowercase: ",x)
print("---------------------------------------------------")

# lstrip() Returns a left trim version of the string
text = "pakistan"
print(text)
x = text.lstrip()
print("lstrip: " "amongst all", x, "is beautiful city.")
print("---------------------------------------------------")


# rstrip() Returns a right trim version of the string
text = "pakistan"
print(text)
x = text.rstrip()
print("rstrip: ""amongst all", x, "is beautiful city.")
print("---------------------------------------------------")

# strip() Returns a trimmed version of the string
text = "    pakistan          "
print(text)
x = text.strip()
print("strip: ""amongst all", x, "is beautiful city.")
print("---------------------------------------------------")

# maketrans() Returns a translation table to be used in translations
text = "pakistan zindabad"
print(text)
x = str.maketrans("a", "e")
print("maketrans: ", text.translate(x))
print("---------------------------------------------------")

# translate() Returns a translated string
text = "pakistan zindabad"
txt = {20:30}
print(text)
print("trans: ", text.translate(text))
print("---------------------------------------------------")

# partition() Returns a tuple where the string is parted into three parts
'''Search for the word "beautiful", and return a tuple with three elements:

1 - everything before the "match"
2 - the "match"
3 - everything after the "match"'''

text = "PAKISTAN ZINDABAD. PAKISTAN IS A BEAUTIFUL CITY"
print(text)
x = text.partition("BEAUTIFUL")
print("PARTITION: ",x)
print("---------------------------------------------------")

# rpartition() Returns a tuple where the string is parted into three parts
text = "PAKISTAN ZINDABAD. PAKISTAN IS A BEAUTIFUL CITY"
print(text)
x = text.rpartition("city")
print("rpartition: ", x)
print("---------------------------------------------------")

# replace() Returns a string where a specified value is replaced with a specified value
text = "PAKISTAN ZINDABAD. PAKISTAN IS A BEAUTIFUL CITY"
print(text)
x = text.replace("BEAUTIFUL","WONDERFUL")
print("REPLACE: ",x)
print("---------------------------------------------------")

# rfind()	 Searches the string for a specified value and returns the last position of where it was found
text = "PAKISTAN ZINDABAD. PAKISTAN IS A BEAUTIFUL CITY"
print(text)
x = text.rfind("BEAUTIFUL")
print("rfind: ",x)
print("---------------------------------------------------")

# rindex() Searches the string for a specified value and returns the last position of where it was found
text = "PAKISTAN ZINDABAD. PAKISTAN IS A BEAUTIFUL CITY"
print(text)
x = text.rindex("BEAUTIFUL")
print("rindex: ",x)
print("---------------------------------------------------")

# rjust() Returns a right justified version of the string
text = "PAKISTAN"
x = text.rjust(100)
print(x, "is beautiful city.")
print("---------------------------------------------------")


# rsplit() Splits the string at the specified separator, and returns a list
text = "PAKISTAN"
x = text.rsplit(",")
print(x, "is beautiful city.")
print("---------------------------------------------------")

# split() Splits the string at the specified separator, and returns a list
text = "pakistan is a beautiful city"
print(text)
x = text.split()
print("splits: ", x)
print("---------------------------------------------------")


# splitlines() Splits the string at line breaks and returns a list
text = "pakistan is \na beautiful city"
print(text)
x = text.splitlines()
print("splitlines: ",x)
print("---------------------------------------------------")


# startswith() Returns true if the string starts with the specified value
text = "pakistan is a beautiful city"
print(text)
x = text.startswith("pakistan")
print("starts with", x)
print("---------------------------------------------------")



# swapcase() Swaps cases, lower case becomes upper case and vice versa
text = "pakistan is a beautiful City"
print(text)
x = text.swapcase()
print("swapcase: ",x)
print("---------------------------------------------------")

# title() Converts the first character of each word to upper case
text = "pakistan is a beautiful city"
print(text)
x = text.title()
print("title: ",x)
print("---------------------------------------------------")

# fill() Fills the string with a specified number of 0 values at the beginning
text = "pakistan is a beautiful city"
print(text)
x = text.zfill(10)
print("zfill: ",x)
print("---------------------------------------------------")
