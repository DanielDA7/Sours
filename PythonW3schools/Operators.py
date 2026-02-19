import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#Создание простого условия if...else

# if 5 == 5:
#     print("True", end="")
#     print("!!!")
# else:
#     print("False")

# #Проверка данных от пользователя

# user_data = int(input("Введите число: "))
# '''
# if user_data > 5:
#     print("Число больше 5")
# elif user_data < 5:
#     print("Число меньше 5")
# '''

# #Форматы проверок
# user_data = int(input("Введите число: "))
# '''
# if user_data > 5:
#     print("Число больше 5")
# elif user_data < 5:
#     print("Число меньше 5")
# '''

# #Вложенные условия
# user_data = int(input("Введите число: "))
# if user_data > 5:
#     print("Число больше 5")
#     if user_data > 10:
#         print("Число больше 10")
#     else:
#         print("Число меньше или равно 10")

# #Проверка булевых переменных
# user_data = int(input("Введите число: "))
# isHappy = True

# if user_data < 5:
#     print("Мы на верном пути")
#     if user_data > 6:
#      print("Число больше 6")

# #Оператор «else»
# isHappy = True

# if isHappy:
#     print("Пользователь счастлив")
# else:
#     print("Пользователь не счастлив")

# #Оператор «elif»
# user_data = int(input("Введите число: "))
# isHappy = True

# if isHappy:
#     print("Пользователь счастлив")
# elif user_data == 5:
#     print("Число = 5")
# elif user_data == 7:
#     print("Число = 7")
# else:
#     print("Пользователь не счастлив")

#Несколько условий


#Тернарный оператор
data = input()

number = 5 if data == "Five" else 0

print(number)

