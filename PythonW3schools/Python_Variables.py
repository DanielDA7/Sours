#VARIABLES
'''
x = 5
y = "John"
print(x)
print(y)
'''
'''
x = 4   # x is of type int
x = "Sally"   # x is now of type str
print(x)
'''
'''
x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)
'''

"""
x = 5
y = "John"
print(type(x))
print(type(y))
"""

#Присваивание Нескольких Значений
"""
x,y,z = "Banana", "Cherry", "Apple"
print(x)
print(y)
print(z)

x=y=z = "Orange"
print(x)
print(y)
print(z)
"""
#Unpack a Collection
"""
fruits = ["apple", "banana", "cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)
"""

#Output Variables
"""
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 28
print(x+y)

"""

#Global Variables
"""
x = "awesome"
def myfunc():
    print("Python is" + x)

myfunc()
"""
#///////
"""
x = " awesome"

def myfunc():
    x = " fantastic"
    print("Python is" + x)

myfunc()

print("Python is" + x)
#///////
def myfunc():
    global x
    x = " fantastic"

myfunc()

print("Python is" + x)
"""

