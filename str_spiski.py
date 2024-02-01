'''
Во многих языках программирования имеются такие данные, которые позволяют хранить набор
объектов, доступных по индексу (номеру вхождения).

Последовательности в Python позволяют хранить
набор объектов как одного типа данных, так и разных.

Причем некоторые из этих наборов (например, списки) могут также увеличиваться или уменьшаться в размерах.
Одним из самых распространенных видов последовательностей является строка — последовательность символов

Строка (str) является неизменяемым типом данных. Это означает, что строковое значение не может быть обновлено. 

При создании переменной, вначале будет создан объект, в состав которого входит уникальный идентификатор, тип и значение. 
Только после этого переменная может ссылаться на уже созданный объект.
Неизменяемость типа данных означает, что созданный объект больше не изменяется. Например, если мы объявим переменную myStr = "hello", то будет создан объект со значением «hello», типа str и идентификатором, который можно узнать с помощью функции id().
'''
# test = '''
# lnnon
# mokmok
# lk'''
# print(test)


# Базовые операции со строками
# 1 Конкатенация
# 2 Дублирование строк (умножение)
# Определение длины строки len()


'''
Теперь рассмотрим методы объекта str (строки). str
(сокращение от «string») — это название типа данных
(объекта) в Python, представляющего из себя последовательность символов (строку).
'''
# objName.methodName(args)
# str.methodName(args)

'''str.capitalize() переводит первый символ строки str
в верхний регистр, остальные — в нижний, возвращаемый результат — преобразованная копия оригинальной строки str (при этом оригинальная строка в результате работы метода не изменится, как и в случае использования рассмотренных ниже методов преобразования регистра).
■ str.lower() переводит все буквенные символы оригинальной строки str в нижний регистр
■ str.upper() преобразует все буквенные символы строки str в верхний регистр
■ str.title() преобразует первые буквы каждого слова в строке str в верхний регистр 
■ str.swapcase() преобразует буквенные символы строки str, меняя их регистр на противоположный'''


# Методы поиска подстроки в строке
myStr = "Python was created in the late 1980's by Guido van Rossum. Python- cool!"

'''count - определяет кол-во вхождений подстроки в строку'''
# print(myStr.count('Python')) 
# print(myStr.count('Python',20,65)) 
# print(myStr.count('Python',10)) 

'''find - возвращает индекс начала первого вхождения фрагмента. -1 если не найдет'''
# print(myStr.find('a')) 
# print(myStr.find('a',2,5)) 

'''index - похож на find. Но вместо -1 вызовет исключение ValueError'''
# print(myStr.index('a')) 
# print(myStr.index('a',2,5))

# str.rfind() - Ищет первое вхождение с конца строки
# str.rindex() - тоже самое что и index. Но с конца строки


# ===========================================
# Методы проверки начала (окончания) строк
'''Методы данной группы возвращают True в случае,
когда оригинальная строка удовлетворяет условию, False —
иначе.'''
'''startswith - — определяет, начинается ли строка str с указанного фрагмента'''
# print(myStr.startswith('P')) 
'''endswith - endswith — определяет, заканчивается ли строка str указанным фрагментом'''
# print(myStr.endswith('l')) 


'''Методы форматирования строк'''
# myStr="Python2021"
'''str.center() дополняет (расширяет) строку str до указанной длины width'''
# print(myStr.center(30))
# print(myStr.center(30,'*'))
# print(myStr.center(5))

'''str.ljust() возвращает выровненную по
левому краю копию строки str указанной ширины'''
# myStr="Python- cool!"
# print(myStr.ljust(20))
# print(myStr.ljust(20,'@'))
# print(myStr.ljust(5))
# print(myStr.rjust(20))
# print(myStr.rjust(20,'@'))
# print(myStr.rjust(5))

# myStr="    Python- cool!     "
# print(myStr.lstrip())
# print(myStr.rstrip())
# print(myStr.strip())
# myStr="@;     Python- cool!     @"
# print(myStr.lstrip('@;'))
# print(myStr.rstrip('@'))
# print(myStr.strip('@'))



'''
Методы проверки строк
Иногда нужно проверить, состоит ли строка из определенных символов, например, цифр. Для решения такого
рода задач предусмотрены следующие методы (все они,
как результат, возвращают значение True — если строка
содержит нужные символы, False — иначе).
■ str.isalnum() — проверяет, состоит ли строка str только
из буквенных и цифровых символов.
■ str.isalpha() — проверяет, состоит ли строка str только
из буквенных символов.
■ str.isdigit() — проверяет, состоит ли строка str только
из цифровых символов (используется для проверки,
является ли строка str числом).
■ str.islower() проверяет, находятся ли все буквенные символы строки str в нижнем регистре (символы строки
str, которые не являются буквой алфавита — игнорируются данной проверкой).
■ str.isspace() проверяет, что в состав строки str входят
только пробельные символы, к которым относятся
символы пробела ' ', табуляции '\t' и перехода на новую строку '\n'.
■ str.istitle() проверяет, начинается ли каждое слово строки str с символа в верхнем регистре.
■ str.isupper() определяет, находятся ли все буквенные
символы строки str в верхнем регистре.
26
Урок 3
■ str.islower() определяет, находятся ли все буквенные
символы строки str в нижнем регистре.
'''


