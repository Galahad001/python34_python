# Словарь, тип данных dict, — это изменяемая коллекция элементов.

'''Каждый элемент словаря состоит из пары ключ:значение'''
'''
 - словари в Python записываются в фигурных скобках {};
 - элементы словаря разделяются запятой;
 - каждый элемент состоит из ключа и значения;
 - между ключом и значением ставится двоеточие :, после двоеточия — пробел;
 - в пределах словаря каждый ключ должен быть уникальным и относиться к неизменяемым типам данных.
'''
'''Ключами словаря могут быть не только строки str, но и значения любых других неизменяемых типов.'''
# status_dict = {
#     'one': 1,       
#     2: 'Число',      
#     (3, 4): 'Кортеж'  
# } 

# print(status_dict[(3, 4)])

# Второй вариант создания
# user = dict(
#     name='Dima',
#     l_name='Strelov',
#     Age=100,
# )
# print(user)


'''Есть и другой вариант синтаксиса dict(): в качестве аргумента в эту функцию можно передать список кортежей (каждый из которых должен состоять из двух элементов), и эти кортежи будут преобразованы в элементы словаря.'''
# product = dict(
#     [
#         ('Бананы', 10), 
#         ('Яблоки', 20), 
#         ('Персики', 100)
#     ]
# )
# print(product)
'''В каждом элементе словаря ключом станет элемент кортежа с индексом [0] (он должен быть объектом неизменяемого типа), а значением для этого ключа будет элемент кортежа с индексом [1].'''
# test = [['1','name']]
# r = dict(test)
# print(r)

# Получить по отдельности ключи, значения и все разом
# for key in user.keys():
#     print('key: ', key, end=' ----- | ')
# print()
# for value in user.values():
#     print('value: ', value, end=' ----- | ')
# print()
# for key,value in user.items():
#     print( '\tkey: ', key , '; value: ', value )


'''
Функция-упаковщик zip() в качестве аргументов принимает любое количество последовательностей, а возвращает объект типа zip — коллекцию кортежей, каждый из которых содержит элементы исходных последовательностей с одинаковыми индексами.
'''
'''Напечатать значение zip невозможно: его содержимое недоступно. Но можно преобразовать zip-коллекцию в список или кортеж'''
# names = ['Ivanov', 'Petrov', 'Sidorov']
# ages = [32, 47, 19]
# result = zip(names, ages)
# # print(tuple(result))
# # print(list(result))
# print(dict(result))

'''Если последовательности, переданные в zip(), не совпадают по длине, ничего не сломается: лишние элементы будут отсечены.'''






# -------------------------------------------------                          -------------------------------------------------
# dict_1 = {
#     'name': "Mia",
#     'age': 100,
#     'test':True
# }
# dict_2 = {
#     'city': 'Moscov'
# }

'''Объединение словарей update() - добавить все элементы второго словаря в первый'''
# dict_1.update(dict_2)
# print(dict_1)

'''Удаление элемента из словаря del'''
# del  dict_1['test']
# print(dict_1)

'''Извлечение элемента из словаря'''
# i = dict_1.pop('test')
# print(i)

'''Получение всех ключей и значений элементов словаря'''
# y = dict_1.keys()
# print(list(y))

# test = dict_1.items()
# print(test)

'''Очистка словаря clear()'''
# dict_1.clear()
# print(dict_1)

'''Копирование словаря copy()'''
# copy_of_dict = dict_1.copy()
# print(copy_of_dict)









# МНОЖЕСТВА
'''Множества — это не последовательности: к элементам множества нельзя обратиться по индексам, порядок элементов в множестве не определён и при каждом обращении может быть разным.'''
'''Создать множество можно перечислив значения в фигурных скобках {}'''
# names = { 'Ivan', 'Alexander', 'Vasya' }
# print(names)

'''Создание через set'''
# spis = ['Ivan', 'Alexander', 'Vasya', 'Ivan', 'Dima']
# set_numb = set(spis)
# print(set_numb)
'''Элементом множества не могут быть данные изменяемых типов, например списки.'''

'''Множество можно создать и из словаря: оно будет содержать только ключи. Ключи словаря — неизменяемые объекты'''

'''Для добавления элемента в множество применяют set.add().'''
# set_numb.add('Ivan')
# set_numb.add('Mira')
# print(set_numb)

'''Удаление элемента множества remove() или set.discard()'''
# set_numb.remove('Mira')
# print(set_numb)

'''Функция set.pop() удаляет и возвращает случайный элемент множества.'''
# p = set_numb.pop()
# print(p)

'''Очистка множества clear()'''



# Пересечение
'''Для поиска пересечения двух множеств применяют оператор & (логическое И).
Выражение с этим оператором возвращает новое множество, в котором будут собраны элементы, одновременно присутствующие в обоих исходных множествах: «верни элементы, которые есть в первом И во втором множествах».       s3 = s1 & s2'''
s1 = {'Moscow', 'Piter','Krasnodar', 'Sochi', 'Vladivostok'}
s2 = {'Sochi', 'Krasnodar', 'Piter', 'Yekaterinburg'}
# s3 = set.intersection(s1, s2)
# print(s3)

'''Объединение - В результате объединения двух множеств (операция «логическое ИЛИ» - |) будет создано новое множество, содержащее все элементы исходных: «верни элементы, которые есть в первом ИЛИ во втором множестве»  | '''
# s3 = set.union(s1, s2)
# print(s3)

'''Разность множеств -  возвращает новое множество, в которое войдут те элементы первого множества, которых нет среди элементов второго: «верни элементы первого множества за вычетом тех, что есть во втором». 
Оператор для поиска разности — обычный минус -.'''
s3 = set.difference(s1, s2)
print(s3)

'''Симметрической разностью двух множеств будет третье множество, каждый элемент которого принадлежит либо первому, либо втором множеству, но не их пересечению: «верни элементы двух множеств, но исключи элементы, которые есть и в первом, и во втором множестве одновременно».
Для поиска симметрической разности применяют оператор «карет» ^.'''
s3 = set.symmetric_difference(s1,s2)
print(s3)