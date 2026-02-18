# TEXT
# print('Hello World!',  end='')
# print('That`s cool')

# NUMBERS
# print(3)
# print(250)
# print(3*5)
# print("I`m Daniel", 18, "Love Python")
# COMMENTS
"""
This is a comment
written in
more than just one line
"""

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
///////
def myfunc():
    global x
    x = " fantastic"

myfunc()

print("Python is" + x)
"""
"""
x = " awesome"

def myfunc():
    global x
    x = " fantastic"

myfunc()
print("Python is" + x)
"""

# # ===== АРИФМЕТИЧЕСКИЕ ОПЕРАТОРЫ =====
# a, b = 10, 3

# print("=== Арифметика ===")
# print(f"{a} + {b} = {a + b}")
# print(f"{a} - {b} = {a - b}")
# print(f"{a} * {b} = {a * b}")
# print(f"{a} / {b} = {a / b:.2f}")
# print(f"{a} // {b} = {a // b}")   # целочисленное деление
# print(f"{a} % {b} = {a % b}")     # остаток от деления
# print(f"{a} ** {b} = {a ** b}")   # возведение в степень

# # ===== ОПЕРАТОРЫ СРАВНЕНИЯ =====
# print("\n=== Сравнение ===")
# print(f"{a} > {b}: {a > b}")
# print(f"{a} < {b}: {a < b}")
# print(f"{a} == {b}: {a == b}")
# print(f"{a} != {b}: {a != b}")
# print(f"{a} >= {b}: {a >= b}")

# # ===== ЛОГИЧЕСКИЕ ОПЕРАТОРЫ =====
# print("\n=== Логика ===")
# x, y = True, False
# print(f"True and False: {x and y}")
# print(f"True or False: {x or y}")
# print(f"not True: {not x}")

# # ===== ОПЕРАТОРЫ ПРИСВАИВАНИЯ =====
# print("\n=== Присваивание ===")
# n = 10
# n += 5;  print(f"n += 5  → {n}")
# n -= 3;  print(f"n -= 3  → {n}")
# n *= 2;  print(f"n *= 2  → {n}")
# n //= 4; print(f"n //= 4 → {n}")

# # ===== ПОБИТОВЫЕ ОПЕРАТОРЫ =====
# print("\n=== Побитовые ===")
# p, q = 0b1010, 0b1100  # 10 и 12
# print(f"AND:  {p} & {q}  = {p & q}")   # 8
# print(f"OR:   {p} | {q}  = {p | q}")   # 14
# print(f"XOR:  {p} ^ {q}  = {p ^ q}")   # 6
# print(f"NOT:  ~{p}       = {~p}")       # -11
# print(f"LEFT SHIFT:  {p} << 1 = {p << 1}")   # 20
# print(f"RIGHT SHIFT: {p} >> 1 = {p >> 1}")   # 5

# # ===== ОПЕРАТОРЫ ПРИНАДЛЕЖНОСТИ И ИДЕНТИФИКАЦИИ =====
# print("\n=== Принадлежность и идентификация ===")
# lst = [1, 2, 3, 4, 5]
# print(f"3 in lst: {3 in lst}")
# print(f"6 not in lst: {6 not in lst}")

# c = a
# print(f"c is a: {c is a}")
# print(f"c is not b: {c is not b}")
