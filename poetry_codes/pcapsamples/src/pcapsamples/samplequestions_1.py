

fruits1 = ['Apple', 'Pear', 'Banana']
# This is a reference copy
fruits2 = fruits1
# This is a shallow copy ,creates a copy
fruits3 = fruits1[:]
 
fruits2[0] = 'Cherry'
fruits3[1] = 'Orange'
 
res = 0
 
for i in (fruits1, fruits2, fruits3):
    print(i)
    print(type(i))
    if i[0] == 'Cherry':
        res += 1
    if i[1] == 'Orange':
        res += 10
 
print(res)
print(len("") == 2)
print(len("''"))
print("''")

str1 = 'Hello'
str2 = 'Hello'
print(id(str1) == id(str2))  # True
print(id(str1))  # e.g. 140539383947452
print(id(str2))  # e.g. 140539383947452 (the same number)


print("---Items in a list----")
my_list = [i for i in range(-2,-1)]
print(my_list)

print("---format float---")
x = 1.23455
print(f"the string is {format(x,'.2f')}")

print("---System Module")
import platform
print(platform.system())
print(platform.processor())
print(platform.version())

print("---Global Variable-----")

def foo(n):
    global m
    # Varible m has to be initialized to be accessable from global scope ,otherwise it is a syntax 
    # error
    m=0
    assert m!=0

    try:
        x = 1/n
    except ArithmeticError:
        raise ArithmeticError
    
try:
    foo(0)
except ArithmeticError:
    m+=2
except:
    m+=1

print(m)

# Creating byte arrays in 3 ways

# 1 - bytearray from a string
my_string = "Python is powerful"
b_array1_string = bytearray(my_string,"utf-8")
print("--bytearray from string")
print(b_array1_string)
# 1 - bytearray from a iterable (the iterable should be integers 0<=x<256)
array4_bytearray = [1,2,3,255]
b_array1_iterable = bytearray(array4_bytearray)
print("--bytearray from iterable")
print(b_array1_iterable)
# 1 - empty bytearray with size
b_array2_size = bytearray(4)
print("--bytearray init with size")
print(b_array2_size)

# Getter/Setter
class A:
    def __init__(self,a):
        self.__a = a
    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self,a):
        self.__a=a

a = A(24)
a.a = 42
print(a.a)

# Trick length questions
print("Tricky length questions")
print(len('\\\\'))  
print(len("''") == 2)
print(len(""))
print("''")

x=2
x= x==x
print(x)


# Tuples in list (Revise tuples unpacking)
print("Printing tuples in list")
data = [(1,2),(3,4),(5,6)]
print ([i for i,j in data])

for i in data:
    x,y = i
    print (x,y)

data = (10, 20, 30, 40, 50, 60)

first, *middle, last = data
print(f"First: {first}")   # Output: First: 10
print(f"Middle: {middle}") # Output: Middle: [20, 30, 40, 50]
print(f"Last: {last}")     # Output: Last: 60

*start, end1, end2 = data
print(f"Start: {start}")   # Output: Start: [10, 20, 30, 40]
print(f"End1: {end1}")     # Output: End1: 50
print(f"End2: {end2}")     # Output: End2: 60

# Using _ to ignore certain elements in tuples
person_info = ("Alice", 30, "Software Engineer")
name, _, profession = person_info

print(f"Name: {name}")       # Output: Name: Alice
print(f"Profession: {profession}") # Output: Profession: Software Engineer

# try block without except ,it will work
def func():
    try:
        print('Monday')  # Monday
    finally:
        print('Friday')  # Friday

func()

# List comprehensions (revise list comprehension)
data = [[3-i for i in range(3)] for j in range(3)]
result = 0
 
# for i in range(3):
#     result += my_list[i][i]
#What is the value of result 
print(result)
data_1=  [ j for j in range(3)]
print(data)
print(data_1)

print("xyz")
print('xyz' in 'uvwxyz')  # False

# Type of some exceptions
# ValueError/ZeroDivisionError/AssertionError

def calculate_inverse(m):
    assert (m!=0),"Division by zero"

    return 1/m

print(calculate_inverse(3))
# Raising same exceptions within try/except

def calculate_inverse_1(m):
    try:
        return 1/m
    except:
        print("Something went wrong")
        # Partial handling of exceptions, after printing the message it again raises same exceptions
        raise

print(calculate_inverse_1(2))
# Exceptions as objects ,Exception class __str__ overridden in a meaningful way

def returnbigger(a,b):
    try:
        if a > b:
            return a
        else:
            return b
    except ValueError as e:
        print("Value error")
        print(e)
    except TypeError as e:
        print("Type error")
        print(e)
    except Exception as e:
        print("General exception")
        print(e)
        return None
    
print(returnbigger(a,5))

# Printing all subclasses
for subclass in BaseException.__subclasses__():
    print(subclass.__name__)

# Exception args
try:
    raise Exception
except Exception as e:
    print(e.args)

try:
    raise Exception("I don't like exceptions","I really don't like exceptions" )
except Exception as e:
    print(e.args)






