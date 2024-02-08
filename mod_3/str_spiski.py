'''Под словом «коллекции» понимают типы данных, которые могут содержать несколько значений. Значения называют «элементы коллекции».'''
'''
Упорядоченные коллекции: последовательности
В упорядоченной коллекции все элементы расположены в определённом порядке, который задаётся при создании коллекции. К любому элементу упорядоченной коллекции можно обратиться по индексу — порядковому номеру элемента; можно напечатать все элементы по очереди — и порядок всегда будет один и тот же. 
Такие коллекции называют последовательностями. 
Основные типы последовательностей:
Строки  — последовательности символов.
Списки  — последовательности, которые могут содержать любые объекты.
Кортежи  — последовательности, аналогичные спискам, но без возможности модификации.
Диапазоны  — последовательность чисел в определённом интервале.
'''

'''
Неупорядоченные коллекции
В неупорядоченных коллекциях невозможно определить, какой элемент первый, а какой последний. Они как груда детских игрушек в ящике: каждый раз вываливаются в разном порядке. 
Эти структуры обычно используются в тех случаях, когда порядок не имеет значения или когда требуется быстрый поиск по значениям: неупорядоченные коллекции записываются в память так, что поиск по ним выполняется гораздо быстрее, чем по упорядоченным.
Множества - set()
'''



# ------------------------------------
list_test = [10, 'hello', True]
'''Списки — это упорядоченные коллекции, которые могут хранить элементы произвольных типов.
 - Элементы в списке имеют строгий порядок. Каждый элемент обладает порядковым номером (Индекс)
 - Элементы спискамогут быть разных типов
'''
# Добавление в список append()
list_test.append('world')
print(list_test)

# Расширение списка extend() - добавит в конец перврго списка, элементв из второго
list_test2 = [1,2,3]
list_test.extend(list_test2)
print(list_test)

# Вставка элемента по индексу: insert()
list_test.insert(1, 'Python')
print(list_test)

# Удаление элемента: remove() - удаляет первое вхождение. Если не найдет вызовет ошибку
list_test.remove(2)
print(list_test)

# Извлечение элемента: pop() - Удаляет элемент из списка. И возвращает его значение. Если не указать индекс удалит последний эллемент списка
test = list_test.pop(1)
print(list_test)
print(test)

# Индекс элемента: index() - Читает список слева направо и возвращает индекс первого найденного элемента 
print(list_test.index('world'))

# Подсчёт количества: list.count()
list_test.append('hello')
print(list_test.count('hello'))

# Сортировка списка: list.sort() - от меньшего к болешему. И наоборот reverse=True
list_test3 = [4,23,5,77,8,90]
# list_test3.sort()
# list_test3.sort(reverse=True)
print(list_test3)

# Инвертирование списка: reverse()
list_test4 = ['apple', 'banana', 'cherry']
list_test4.reverse()
print(list_test4)

# Копирование списка: copy()
list_test5 = [1,2,3,4,5]
copy = list_test5.copy()
print(copy)
list_test5.append(6)
print(copy)
print(list_test5)
# # ++++++++
# test2 = list_test5
# print(list_test5)
# print(test2)
# list_test5.append(6)
# print(list_test5)
# print(test2)

# Очистка списка: clear()
list_test6 = [1,2,3,4,5]
list_test6.clear()
print(list_test6)



# СБОРЩИК МУСОРА
# Данные, которые невозможно применить повторно, Python воспринимает как «мусор». При появлении мусора за дело берётся специальная программа — сборщик мусора. Она очищает оперативную память, освобождая ячейки для последующего использования.

'''
Если же значение присвоить переменной, картина будет иной. В памяти устройства будет выделена ячейка, в которую будет записано это значение. Переменная при этом будет ссылаться на эту ячейку памяти.
Переменные в Python не хранят значения, а выступают в роли ссылок на ячейки памяти, в которых хранятся значения этих переменных.
Если на ячейку памяти есть ссылка, сборщик мусора не станет очищать эту ячейку: он поймёт, что эти данные нужны программе, и не будет их удалять.
У каждой ячейки памяти есть уникальный идентификатор — адрес, на который и ссылается переменная. Этот идентификатор можно увидеть при помощи встроенной функции id().
'''

'''
Изменяемые и неизменяемые типы данных
Если изменить значение переменной изменяемого типа, будет изменено значение в той ячейке памяти, на которую ссылалась переменная. При этом сама переменная так и будет ссылаться на эту ячейку. Для изменения значений таких переменных применяются специальные функции.

Изменить значение переменной неизменяемого типа невозможно технически: для этого просто нет инструментов. Такие переменные можно только переопределить — объявить заново. Но при этом новое значение будет записано в новую ячейку памяти; переменная станет ссылаться на новую ячейку.
'''

'''
Изменяемые типы данных - это такие типы данных, которые можно изменять после того, как они были созданы. Например, если у вас есть список, вы можете добавлять, удалять или изменять элементы этого списка.
Неизменяемые типы данных, наоборот, не могут быть изменены после создания
'''
testr = [1,2,3,4]
print(f"У списка {testr} - id: {id(testr)}")
testr.append(5)
print(f"У списка {testr} - id: {id(testr)}")

message = "HELLO"
print(f"У строки {message} - id: {id(message)}")
# message[0] = "Y"
message = 'TEST'
print(f"У строки {message} - id: {id(message)}")

i = 1
j = 1
print(f"i = {id(i)}, j = {id(j)}")

# Неизменяемые типы (а это, например, целые числа, числа с плавающей точкой, строки, кортежи — и не только):
# Изменяемые типы (например, списки):
