import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


#Практика 1. Числовые типы данных
number = 5

digit = -3.345323235
word = "Hello World"
boolean = True
print(type(number))
print(str(number), word)

del number

number = 7
print("Результат:", number)

#Мини задача 1. Числовые типы данных
num1=input("Введите первое число: ")
num2=input("Введите второе число: ")
print("Сумма чисел:", int(num1) + int(num2))
print("Разность чисел:", int(num1) - int(num2))
print("Произведение чисел:", int(num1) * int(num2))
print("Частное чисел:", int(num1) / int(num2))
print("Целочисленное деление чисел:", int(num1) // int(num2))
print("Остаток от деления чисел:", int(num1) % int(num2))

