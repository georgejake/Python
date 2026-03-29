
import sys
# Lambda-Map

map_result = map(lambda x: x*2,[1,2,3,4])
# This just prints an iterator
print(map_result)
# To make it readable we need to convert to list
print(list(map_result))
#  watch out !!!!! printing again causes empty list
print(list(map_result))
for element in map_result:
    print(element)
#Lambda - filter ,for filter the function should return boolean

filter_result = filter (lambda x: x%2==0,[1,2,3,4,5])
print(list(filter_result))
# Dictionary sorting

data = {'z': 23, 'x': 7, 'y': 42}
 
for _ in sorted(data):
    print(_)
    print(data[_], end=' ')

# Nested dictionaries
box = {}
jars = {}
crates = {}
 
box['biscuit'] = 1
box['cake'] = 3
 
jars['jam'] = 4
 
crates['box'] = box
crates['jars'] = jars
print(crates)
 
# print(len(crates[box]))
print(len(crates['box']))
# Strings value comparison
print('mike' > 'Mike')

# Division by boolean

w = 7
x = 3
y = 4
z = True
a = w + x * y #19
b = w + x / z #10


# if ???:
#     print('TRUE')
# else:
#     print('FALSE')

print(sys.path)


class A:
 
    A = 23
 
    def __init__(self):
        self.a = 42
 
 
print(hasattr(A, 'A'))

# Closures - Revise
def o(p):
    def q():
        return '*' * p
    return q
 
 
r = o(1)
s = o(2)
print(r() + s())

# __iter__ and __next__

string1 = 'apple'+'orange'
print(string1)

#slicing lists - this will replace every other values
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# below statement will give error as the slice is only for 5
# x[::2] = 10, 20, 30, 40, 50,60
x[::2] = 10, 20, 30, 40, 50

print(x)

x=10
print(bool(x)+True)

data1 = 'a', 'b'
data2 = ('a', 'b')
print(data1)
print(data1 == data2)

# Boolean operators
print("Boolean-values")
print(not 0)
print(not 23)
print(not '')
print(not 'Peter')
print(not None)

# Generators - yield function
# let's find squares upto n 

print("squares")
def findsquares(n):
    i = 1
    while i<=n:                
        yield i * i
        i +=1
# values = findsquares(10)
# print(values.__next__())
# print(values.__next__())
# print(values.__next__())

for i in findsquares(10):
    print(i)

#data length
data = [1, 2, 3, None, (), [], ]

for i in data:
    print(i)
print(len(data))

# num = int(float(input("Please enter a number")))
# print(num)

# finally return
def func():
    try:
        return 1
    finally:
        return 2
 
res = func()
print("Finally return")
print(res)

# Tuple slicing
# data = (1, 2, 4, 8)
data = [1, 2, 4, 8]
data = data[-3:-1]
data = data[:]
print(data)
# getting keys from dictionary
data = {'Peter': 30, 'Paul': 31}
print(list(data.keys()))

#Identity 

list1 = [3, 7, 23, 42]
list2 = [3, 7, 23, 42]
print(list1 is list2)
print(list1 == list2)

print(1,2,4,)



try:
    print("5" / 0)
except ArithmeticError:
    print("arith")
except ZeroDivisionError:
    print("zero")
except Exception as e:
    print("some")
    print(e)

# Class variables

print("Class variables")
class Class:
    Variable = 0
    def __init__(self):
        self.value = 0

'''
However, modifying a class variable through an 
object can lead to unexpected behavior if not handled carefully. 
If you assign a new value to a class variable using an object
 (e.g., obj.class_var = "new value"), you are actually creating a new instance variable
   with that name on the obj instance, rather than modifying the original class variable. 
   The original class variable remains unchanged for other instances and when accessed directly
     via the class name.
To modify the class variable for all instances, 
you should always modify it using the class name (e.g., MyClass.class_var = "new value").
''' 
object_1 = Class()
# Class.Variable +=1
object_1.Variable += 1

object_2 = Class()
object_2.value += 1

print(object_2.Variable + object_1.value)

# Printing length of an empty string
x="i""fool "
print(x)
print(len("""""") == 0)

# passing by vaue and reference
def func(data):
    # below data is local variable and has no relation with the incoming parameter ,though their names are same
    # but if below new declaration is not there ,then it refers to the incoming parameter "data"
    data = [7, 23, 42]
    # paramdata = data
    # del paramdata[0]
    print('Function scope: ', data)  # [7, 23, 42]
 
 
data = ['Peter', 'Paul', 'Mary']
func(data)
print('Outer scope: ', data)  # ['Peter', 'Paul', 'Mary']

# Exam question

string = 'python'[::2]
string = string[-1]+string[-2]
print(string)