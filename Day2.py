#Типы данных в Python
"""
number = 5

digit = -4.32435
word = "Result:"
boolean = True

str_num = "5"

# print(word + str(digit))
print(number + int(str_num))

del number

number = 7
print(word + str(number))
"""

# Задача №1
"""
num1 = int(input("Enter first number: "))

num2 = int(input("Enter second number: "))

num1+=5

print("Result:", num1 + num2)
print("Result:", num1 - num2)
print("Result:", num1 / num2)
print("Result:", num1 * num2)
print("Result:", num1 ** num2)
print("Result:", num1 // num2)

word = "Hi"
print(word * 2)

word = "Zoz"
print(word * 4)
"""

"""
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
"""

#Операторы
"""
print(10+5)

if 5==5:
    print("Yes ", end="")
    print("!!!")
"""

a = 7
b = 3
s = "python"

E1 = a / b
E2 = a // b
E3 = a % b
E4 = a ** b
E5 = (a > b) and (b != 0)
E6 = (a < 0) or (b > 0) and (a == 7)
E7 = "py" in s and "on" in s
E8 = a == 7 == b
E9 = not a == b
E10 = (a + b) * 2 >= 20

print(E1, type(E1))
print(E2, type(E2))
print(E3, type(E3))
print(E4, type(E4))
print(E5, type(E5))
print(E6, type(E6))
print(E7, type(E7))
print(E8, type(E8))
print(E9, type(E9))
print(E10, type(E10))

