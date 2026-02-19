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

# x = " awesome"

# def myfunc():
#     global x
#     x = " fantastic"

# myfunc()
# print("Python is" + x)

import sys
import random

sys.stdout.reconfigure(encoding='utf-8')

def get_random_advice():
    ...

import random

def get_random_advice():
    """Возвращает случайный совет для продуктивности"""
    advices = [
        "Делай небольшие перерывы каждые 25 минут",
        "Пей больше воды, это улучшает концентрацию",
        "Начни день с самой сложной задачи",
        "Не проверяй социальные сети перед работой",
        "Установи режим без уведомлений",
        "Спи не менее 7 часов в сутки",
        "Двигайся больше, сидение — вредно",
        "Завтракай полноценно каждое утро",
    ]
    return random.choice(advices)

def main():
    print("=== Генератор советов ===\n")
    
    while True:
        print(f"💡 Совет: {get_random_advice()}\n")
        
        choice = input("Хочешь ещё совет? (да/нет): ").lower()
        if choice not in ['да', 'yes', 'y']:
            print("Удачи в работе! 🚀")
            break

if __name__ == "__main__":
    main()