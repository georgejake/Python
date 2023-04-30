# Basic variable assignment ,Calculating area of a triangle
import json

base = 12
height = 10
area = 1 / 2 * (base * height)
print(type(area))
print("area of this triange is", area)
# Dictionaries in Python ,Dictionary cannot have key value pairs
"""
Deleting/Adding/Printing and Looping a dictionary/Checking key in
Dictionary is also the JSON formatting in python
"""
d = {"george": "1234", "ditta": "1234", "diya": 123, "dhwani": 345}
print(d["george"])
print(d)
del d["george"]
d["george"] = "1234"
print("george" in d)
for key in d:
    print(key)
    print(d[key])
for k, v in d.items():
    print("Key is:", k, "Value is:", v)
# Functions
"""
Parameters can be passed by position and by name. There is also provision to provide optional parameter
"""


def total_cost(exp):
    total = 0
    for item in exp:
        total = total + item
    return total


def sum(a, b=1):
    return a + b


joe_explist = [100, 200, 300]
print(total_cost(joe_explist))
print(sum(a=3, b=4))
print(sum(a=3))

# Read input from console
"""
Get remainder function, Equality is checked using ==, Convert string to integer
"""
a = input("Enter a number")
a = int(a)
if a % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")
# JSON
"""
In PYTHON ,Dictionary closely resembles json. 
Initialize a JSON, Dump JSON to string,Dump JSON to a file, Read JSON document and parse
"""
books = {}
books["tom"] = {
    'name': 'tom',
    'address': '1 read street,NY',
    'phone': 1234
}
books["george"] = {
    'name': 'george',
    'address': '1 green street,NY',
    'phone': 5678
}
print(books)
s = json.dumps(books)
print(s)
# Writing to file
with open("/MyFiles/HelloJson", "w") as f:
    f.write(s)
# Reading from file
f = open("/MyFiles/HelloJson", "r")
s = f.read()
print(s)
loadedBook = json.loads(s)
print(loadedBook['tom'])
print(loadedBook['tom']['phone'])

for person in books:
    #This only prints tom & george ,basically the keys
    print(person)
    print(books[person])

#List in python
"""
List are fundamental building block of collections in python
Lists are one of 4 built-in data types in Python used to store collections of data, 
the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
List Constructor - Note the double round-brackets
"""
indian = ["samosas", "dal", "chapathi"]
italian = ["pasta", "pista", "rosetti"]
chinese = ["fried rice", "noodles", "manchurian"]

dish = input("Enter the dish name: ")
if dish in indian:
    print("Indian Cusine")
elif dish in italian:
    print("Italian cusine")
elif dish in chinese:
    print("Chinese cusine")
else:
    print("Sorry!!! I dont know")

thislist = list(("apple", "banana", "cherry"))
print(thislist)
#Loops

