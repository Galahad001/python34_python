# Операции сравнения
    # Операции сравнения используются для создания условий на основании сравнения элементов. Элементы,
    # к которым применяется операция, называют операндами. 
print(2 > 1)
print(2 < 1)
print(2 >= 1)
print(2 <= 1)
print(2 == 1)
print(2 != 1)

# Python - может привести любое значение типа к логическому 
# Строка без символов, 0, None, пустые списки, кортежи, словари - будут преведены к False

# Строки с символами, числа отличные от 0, списки,кортежи,словари с элементами - будут преведены к True
print('---------------')
print(bool(''))
print(bool('asd'))
print(bool(0))
print(bool(1))
print(bool([]))
print(bool([1,2,3]))




print('---------------')
# Логические операции
# Логические операции позволяют комбинировать несколько логических выражений в одно.
# and («Логическое умножение) - вернет True если оба выражения равны
print(True and False)
# or «Логическое сложение» - возвращает True, если хотя бы
# одно из выражений равно True
print(True or False)
# «Логическое отрицание»: возвращает значение, обратное операнду.
print(not True)


# time = int(input("Введите текущее время в часах "))% 24
# ticket = False
# money = True
# luggage = False
# print(money or ticket and not luggage and time > 6)


# Известно, что високосным годом считается тот год,
# который кратен 4, не кратен 100 или кратен 400.
# year = 2000
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#  print("Year", year, "is leap")


speed = 50

if speed < 60:
    print('Скорость в пределах 60км/ч')
    speed += 10
if speed > 60:
    print('Превышение скорочти')
else:
    print('Едешь прям четко 60')


# Рассмотрим практическое применение вложенных
# конструкций на примере копилки
# abs - получаем модуль числа. Откидываем знаки
# account = int(input("Введите сумму, которую вы положили: "))
# account = abs(account)
# if account > 0:
#     withdrawal = int(input("Введите, сколько вы берете: "))
#     withdrawal = abs(withdrawal)
#     if withdrawal < account:
#         account -= withdrawal
#         print("Вы взяли", withdrawal, ".")
#         print("Осталось", account, "в копилке.")
#     else:
#         print("Есть только", account, ".")
# else:
#     print("В копилке нет денег")
    


'''Исключения — один из двух основных типов ошибок
в программировании. В отличие от синтаксических ошибок, которые возникают во время написания, исключения
могут появиться во время выполнения программы.'''
'''     Типы исключений
У каждого исключения есть собственный тип, который
определяется тем, какая ошибка его вызвала, и дает возможность по-разному реагировать на различные виды ошибок.
■ BaseException — базовый тип, из которого происходят все остальные, в том числе системные:
    • Exception — базовый тип для «стандартных» и пользовательских исключений:
        ▫ ArithmeticError — арифметическая ошибка:
        ▫ OverflowError  — возникает, когда результат арифметической операции слишком велик для представления;
    • ZeroDivisionError — деление на ноль.

■ ImportError — импортировать модуль или его атрибут не удалось;

■ LookupError — некорректный индекс или ключ:
    • IndexError — индекс не входит в диапазон элементов;
    • KeyError  — несуществующий ключ (например,в словаре).

■ NameError — не найдено переменной с указанным именем;

■ RuntimeError — возникает, когда исключение не попадает ни под одну из других категорий;

■ SyntaxError — синтаксическая ошибка:
    • IndentationError — неправильные отступы:
        ▫ TabError  — смешивание в  отступах табуляции и пробелов.

■ TypeError — операция применена к объекту несоответствующего типа;

■ ValueError — функция получает аргумент правильного типа, но некорректного значения.'''

'''
BaseException: базовый тип для всех встроенных исключений

Exception: базовый тип, который обычно применяется для создания своих типов исключений

ArithmeticError: базовый тип для исключений, связанных с арифметическими операциями (OverflowError, ZeroDivisionError, FloatingPointError).

BufferError: тип исключения, которое возникает при невозможности выполнить операцию с буффером

LookupError: базовый тип для исключений, которое возникают при обращении в коллекциях по некорректному ключу или индексу (например, IndexError, KeyError)
'''

'''
IndexError: исключение возникает, если индекс при обращении к элементу коллекции находится вне допустимого диапазона

KeyError: возникает, если в словаре отсутствует ключ, по которому происходит обращение к элементу словаря.

OverflowError: возникает, если результат арифметической операции не может быть представлен текущим числовым типом (обычно типом float).

RecursionError: возникает, если превышена допустимая глубина рекурсии.

TypeError: возникает, если операция или функция применяется к значению недопустимого типа.

ValueError: возникает, если операция или функция получают объект корректного типа с некорректным значением.

ZeroDivisionError: возникает при делении на ноль.

NotImplementedError: тип исключения для указания, что какие-то методы класса не реализованы

ModuleNotFoundError: возникает при при невозможности найти модуль при его импорте директивой import

OSError: тип исключений, которые генерируются при возникновении ошибок системы (например, невозможно найти файл, память диска заполнена и т.д.)
'''

# Перехват исключений
# try except
# В блок try - помещается набор иструкция в которых возможно возникнет исключение
# В блок except - помещается набор инструкций для обработки этого исключения

# Допустим на склад поступили товары. Надо указать количество и вид товара.
# try:
#     tov_col = int(input('Введите сумму полученого товара '))
#     tov_name = input('Введите категорию товара ')
#     num = int(input('На сколько отделов полжен уйти полученый товар '))
#     res = tov_col // num
#     print('На', num, 'отдела уйдет по', res,'полученых товаров')
# except ValueError:
#     print('Сумма должна быть числом')
# except ZeroDivisionError:
#     print('Нельзя делить постаку на 0 частей')
# Кроме того, конструкцией «try … except» предусмотрен
# блок «finally», инструкции которого будут выполнены
# вне зависимости от того, возникнет исключение или нет
#     Блок «finally» используется в том случае, когда нам
# необходимо гарантировать окончание работы программы.
# finally:
#       print('Завершение программы')




# Вызов исключений
'''В Python мы можем не только перехватывать исключения, но и напрямую вызывать их. Для этого необходимо
использовать ключевое слово «raise». С помощью «raise» мы можем указать, к какому типу будет принадлежать
вызванное исключение:'''

# try:
#     apple = int(input('Введите количкство яблок '))
    
#     if apple < 0:
#         raise Exception
#     print('У вас', apple, 'яблок')
# except Exception:
#     print('Не может быть яблок меньше 0')
    

'''
Одной из главных особенностей работы с «try … except»
является правильное расположение блоков «except».
«ZeroDivisionError» является подтипом «ArithmeticError»,
а «ValueError» — подтипом «Exception»
'''
try:
    raise ValueError
except Exception:
    print('Ошибка')
except ValueError:
    print('Текст ошибки ValueError')
'''«ValueError» является подтипом «Exception», возникшее
исключение будет обработано первым блоком, а второй,
предназначенный для обработки исключений такого
типа, выполнен не будет. Для того, чтобы исправить это,
необходимо изменить порядок следования блоков except.
Общие типы исключений должны быть расположены
ниже частных'''

try:
    raise ArithmeticError
except ZeroDivisionError:
    print('Ошибка ZeroDivisionError')
except ArithmeticError:
    print('Ошибка ArithmeticError')


# Блок exept для нескольких типов исключений
# Python так же позволяет один блок «exept» для разных
# типов исключений.
# try:
#     tov_col = int(input('Введите сумму полученого товара '))
#     tov_name = input('Введите категорию товара ')
#     num = int(input('На сколько отделов полжен уйти полученый товар '))
#     res = tov_col // num
#     print('На', num, 'отдела уйдет по', res,'полученых товаров')
# except (ValueError, ZeroDivisionError):
#     print('ERROR')


print('-------------')
# Ошибки можно присвоить переменным с помощью as
try:
    x = 1 / 0
except Exception as test:
    print(test)

try:
    raise ValueError('Ошибка некоретного значениня')
except ValueError as t:
    print(t)






# Ежедневно каждый из нас сталкивается с циклами — процессом выполнения однотипных действий. 
# Итерация — отдельное повторение однотипного действия, под которым понимается блок выполнения цикла («тела цикла»).
'''Цикл while
В первую очередь рассмотрим цикл «while», синтаксис
которого идентичен конструкции «if». Этот цикл повторяет
выполнение тела цикла до тех пор, пока соответствующее
условие не окажется ложным '''
# Попробуем найти сумму всех целых чисел расположенных между «х1» и «х2».
# x1 = int(input("Enter x1: "))
# x2 = int(input("Enter x2: "))
# x = x1 + 1
# sum = 0
# while x < x2:
#     sum += x
#     x += 1
# print("The sum of all integers between", x1, "and", x2, "is", sum)

# Циклы типа «for», в отличие от «while», повторяются
# не в зависимости от выполнения условия, а для каждого
# элемента в списке, множества, кортежа или другой совокупности элементов.
# message = input('Введите сообщение ')
# for i in message:
#     print(i)

# Цикл может пройти по строке частично. Для этого
# необходимо её разделить при помощи оператора среза
# «[::]»
# message2 = input('Введите сообщение ')
# for i in message2[::-1]:
#     print(i)


# Циклы бывают вложеные друг в друга
# for i in range(1, 11):
#     print()
#     for j in range(1, 11):
#         print(f'{i} * {j} =', i*j)