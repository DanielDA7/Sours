#Работа со списками
'''
 nums = [1, 2, 3, 4, 5, "Hello", True, [9, 8, 7]]
 nums[6]=False
 nums[0]=10
 print(nums[-1][1])
'''

#Функции для работы со списками
'''
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.insert(0, 0)
numbers.extend([7, 8, 9])
# numbers.reverse()
numbers.pop()
numbers.remove(6)
# numbers.clear()

print(numbers.count(3))
print(len(numbers))
'''

#Вывод списка через цикл
'''
nums = [5,2,7,"Hello", True]
for i in nums:
    print(i)
'''
#Наполнение списка от пользователя
'''
n = int(input("Введите длину списка: "))
user_list = []
i = 0

while i < n:
    string = input(f"Введите элемент списка #{i+1}: ")
    user_list.append(string)
    i += 1

print(user_list)
'''

#Проверка на чётность и нечётность
numbers = [1, 4, 7, 12, 19, 22, 35, 48]
for i in numbers:
    if i % 2 == 0:
        print(f"Чётные: {i}")
    else:
        print(f"Нечётные: {i}")

# Ожидаемый результат:
# Чётные: [4, 12, 22, 48]
# Нечётные: [1, 7, 19, 35]
