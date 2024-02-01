'''
Пользователь вводит с клавиатуры строку. Произведите поворот строк и полученный результат выведите
на экран
'''
# message = input('Введите текст ')
# print(message[::-1])


'''Пользователь вводит с клавиатуры строку. Посчитайте количество букв, цифр в строке. Выведите оба
количества на экран.'''
# message = input('Введите текст ')
# count_num = 0
# count_str = 0
# no_str_and_num = 0

# for i in range(len(message)):
#     if message[i].isdigit():
#         count_num += 1
#     elif message[i].isalpha():
#         count_str += 1
#     elif message[i].isdigit()  == False and message[i].isalpha() == False:
#         no_str_and_num += 1
    
# print(f'Строка {count_str}')
# print(f'Число {count_num}')
# print(f'Не число и не строка {no_str_and_num}')


'''
Пользователь вводит с клавиатуры строку и символ
для поиска. Посчитайте сколько раз в строке встречается
искомый символ. Полученное число выведите на экран.
'''
# message = input('Введите текст ')
# what = input('Что ищем? ')

# count = message.count(what)

# print(count)



'''
Пользователь вводит с клавиатуры строку, слово для поиска, слово для замены. Произведите в строке замену одного слова на другое. Полученную строку отобразите на экране. Дай простое решение
'''
message = input('Введите текст ')
what = input('Что ищем? ')

# res = message.split(' ')
# for i in range(len(res)):
#     if res[i].lower() == what.lower():
#         res[i] = "TEST"

# print(' '.join(res))

print(message.replace(what,  'TEST'))