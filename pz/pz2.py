'''
    Пользователь вводит с клавиатуры целое шестизначное число. Написать программу, которая определяет,
является ли введенное число — счастливым (Счастливым считается шестизначное число, у которого сумма
первых 3 цифр равна сумме вторых трех цифр).
С другой стороны 378423 несчастливое число, так
как 3+7+8 != 4+2+3.Если пользователь ввел не шестизначное число требуется вывести сообщение об ошибке.
'''
# number = input('Введите  шестизначное число: ')
# if len(number) == 6:
#     num1 = int(number[:3])
#     num2 = int(number[3:])

#     res_num1 = (num1 // 100) + (num1  % 100 // 10) + (num1 % 10)
#     res_num2 = (num2 // 100) + (num2  % 100 // 10) + (num2 % 10)
    
#     if res_num1 == res_num2:
#         print('Число счатливое')
#     else:
#         print('Число не счастливое')
# else:
#     print('Неправильный Ввод')



'''
Пользователь вводитшестизначное число.Необходимо поменять первую и шестую цифры,
вторую и пятую цифры.
Например, 723895 должно превратиться в 593827.
Если пользователь ввел не шестизначное число требуется вывести сообщение об ошибке.
'''
# number = input('Введите шестизначное число: ')

# if len(number) == 6:
#     num1 = (int(number)  // 100000) % 10 
#     num2 = (int(number)  //  10000) % 10
#     num3 = int(number) % 100 // 10
#     num4 = int(number) % 10
    
#     new_num = str(num4) + str(num3) + number[2:4] + str(num2) + str(num1)
#     print(new_num)
    # print(num1)
    # print(num2)
    # print(num3)
    # print(num4)
# print(723895 % 10)
# print(723895 % 100 //10)
# print(723895 // 100000)
# print(723895 // 10000 % 10)



'''
Пользователь вводит с клавиатуры два числа. Нужно
посчитать сумму чисел в указанном диапазоне, а также
среднеарифметическое.
'''
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))

# sum = 0
# count = 0
# for i in range(a, b):
#     sum += i
#     count += 1
# print(f'Сумма диапазона {sum}, среднеарифметическое {sum / count}')


'''
дание 2
Пользователь вводит с клавиатуры число. Требуется
посчитать факториал числа. Например, если введено 3,
факториал числа 1*2*3 = 6.
Формула для расчета факториала: n! = 1*2*3…*n,где
n — число для расчета факториала.
'''
# number = int(input('Введите число - '))

# fact = 1
# for i in range(1, number+1):
#     fact *= i
# print(fact)


'''
Пользователь вводит с клавиатуры длину линии и
символ для заполнения линии. Нужно отобразить на
экране горизонтальную линию из введенного символа,
указанной длины.
Например, если было введено 5 и &, тогда вывод на
экран будет такой: &&&&&.
'''
# number = int(input('Введите число '))
# symbol = input('Введите символ ')
# s = ''
# while number > 0:
#     s += symbol
#     number -= 1
# print(s)



'''
Показать таблицу умножения для числа, введенного
пользователем. Например, если пользователь вводит
число 7, нужно показать:
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
'''
# number = int(input("Введите число: "))
# for i in range (1, 11):
#     print(f'{i} * {number} = {i * number}')



'''
Написать программу – конвертер валют. Реализовать
общение с пользователем через меню.

 Из	      В	        Формула (сумма * курс_из / курс_в)
Доллар   (90.18 руб)	Рубль	сумма * 90.18 / 1
Рубль	 Доллар (90.18 руб)	сумма * 1 / 90.18
'''
# EUR = 0.92
# USD = 1.08 

# many = int(input('Введите сумму: '))
# currency_from = int(input('1 - из евро в доллоры; 2 - из доллора в евро '))

# if currency_from == 1:
#     print(many *  USD / 1)
# elif currency_from == 2:
#     print(many *  EUR / 1)


'''
Пользователь вводит с клавиатуры две границы диапазона и число. Если число не попадает в диапазон,
программа просит пользователя повторно ввести число,
и так до тех пор, пока он не введет число правильно. Программа отображает все числа диапазона, выделяя число
восклицательными знаками. Например:
1 2 3 !4! 5 6 7.
'''

# result = ''
# while True:
#     a = int(input('Мин число диапазона = '))
#     b = int(input('Мак число диапазона = '))
#     c = int(input('Число в диапазоне = '))

#     if  c >= a and c <= b:
#         for i in range(a,b):
#             if  i == c:
#                 result += "!" + str(c) + "! "
#                 continue
#             result +=  str(i) + ' '
#         print(result)
#         break
#     else:
#         print('Число не в диапазоне')
#         continue


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Написать игру «Угадай число». Программа загадывает число в диапазоне от 1 до 500.
Пользователь пытается его угадать. 
После каждой попытки программа выдает подсказки, больше или меньше его число загаданного. 
В конце программа выдает статистику за сколько попыток угадано число, сколько времени это заняло. Предусмотреть выход по 0 в случае, если пользователю надоело угадывать число.
'''
# import random
# random_number = random.randint(1, 500)

# count = 0

# while True:
#     print('0 - для выхода')
#     user_guess = int(input("Введите число от 1 до 500 = "))
#     if  user_guess == 0:
#         break
#     count += 1
#     if user_guess > random_number:
#         print("Твое число больше")
#     elif  user_guess < random_number:
#         print("Твое число меньше")
#     else:
#         print(f"Твой номер {user_guess} равен числу компьютера")
#         break

# print(f'Попыток {count}')

'''
Пользователь вводит с клавиатуры размер стороны
квадрата. Требуется отобразить на экран заполненный
квадрат. Размер стороны равен введённому размеру.
Например, если пользователь ввёл 3 на экране будет
выведено:
***
***
***
'''
# i =  int(input('Ввод размера стороны квадрата '))
# res = i
# while res > 0:
#     print("* " * i)
#     res -= 1


'''
Пользователь вводит с клавиатуры ширину и высоту прямоугольника. Требуется отобразить на экран
заполненный прямоугольник с указанными высотой и
шириной. Например, если пользователь ввёл высоту 3,
а ширину 5 на экране будет выведено:
*****
*****
*****
'''
# v = int(input('Введите высоту - '))
# s = int(input('Введите ширину - '))

# while v > 0: 
#     print("* " * s)
#     v -= 1



'''
Пользователь вводит с клавиатуры размер стороны
квадрата. Требуется отобразить на экран незаполненный 
квадрат (отображаются только границы квадрата).
Размер стороны равен введённому размеру
'''
# number = int(input('Введите длину стороны  квадрата: '))
# for i in range(0, number):
#     # print('-')
#     for j in range(0, number):
#         if i == 0 or j == 0 or i == number-1 or j == number-1:
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print("")


'''
Пользователь вводит с клавиатуры длину и ширину
прямоугольника. Требуется отобразить на экран незаполненный прямоугольник (отображаются только границы прямоугольника). 
Размер длины и ширины равен введенным данным.
'''
# num1 = int(input('Введите длину : '))
# num2 = int(input('Введите ширину : '))
# for i in range(0, num1):
#     # print('-')
#     for j in range(0, num2):
#         if i == 0 or j == 0 or i == num1-1 or j == num2-1:
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print("")



'''
Пользователь вводит число. Определить количество
цифр в этом числе, посчитать их сумму и среднее арифметическое. Определить количество нулей в этом числе.
Общение с пользователем организовать через меню.
'''
# number = int(input('Введите число '))
# sum_n = 0
# count = 0
# zero = 0

# for i in str(number):
#     count += 1
#     sum_n += int(i)
#     if int(i) == 0:
#         zero += 1
    
# print(f'Сумма {sum_n}. Среднее {sum_n / count}. Нулей {zero} ')


'''
Написать программу, которая выводит на экран
шахматную доску с заданным размером клеточки. Например, три,
***---***---***---***---
***---***---***---***---
***---***---***---***---
---***---***---***---***
---***---***---***---***
---***---***---***---***
'''
# for i in range(0,8):
#     s =''
#     for j in range(0, 4):
#         if not i % 2 :
#             s += '***___' 
#         else:


'''
Написать программу, которая проверяет пользователя
на знание таблицы умножения. Программа выводит на
экран два числа, пользователь должен ввести их произведение. Разработать несколько уровней сложности (от
личаются сложностью и количеством вопросов). Вывести
пользователю оценку его знаний.
'''
# import random

# while True:
#     ur = int(input('Уровень сложности 1 - лекго, 2 - средне 3 - сложно'))

#     if ur == 1:
#         numb1 = random.randint(1, 3)
#         numb2  = random.randint(1, 10)

#         user = int(input(f'{numb1} * {numb2} = ? '))
#         if user == numb1*numb2:
#             print('Правильно')
#             v =input('Выйти? да/нет: ')
#             if v == 'да':
#                 break
#         else:
#             print('Неправильно')

#     elif ur == 2:
#         numb1 = random.randint(4, 10)
#         numb2  = random.randint(1, 10)

#         user = int(input(f'{numb1} * {numb2} = ? '))
#         if user == numb1*numb2:
#             print('Правильно')
#             v =input('Выйти? да/нет: ')
#             if v == 'да':
#                 break
#         else:
#             print('Неправильно')

#     elif ur == 3:
#         numb1 = random.randint(1, 10)
#         numb2  = random.randint(1, 10)
#         numb3  = random.randint(1, 10)

#         user = int(input(f'{numb1} * {numb2} * {numb3} = ? '))
#         if user == numb1*numb2*numb3:
#             print('Правильно')
#             v =input('Выйти? да/нет: ')
#             if v == 'да':
#                 break
#         else:
#             print('Неправильно')
#     else:
#         print("Ошибка ввода")




number = int(input("Высота ромба "))
for x in range(0, number):
    print(" " * (number - x), "*" * (2*x + 1))
for x in range( number - 2, -1, -1):
    print(" " * (number - x), "*" * (2*x + 1))