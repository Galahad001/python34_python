'''
Создайте функцию для отображения текущего времени.
Функция не принимает параметров. Функция не используя синтаксис декораторов, произведите декорирование функции с помощью другой функции. Потенциальный вывод данных на экран:
***********************
23:00
***********************
В этом выводе на экран две линии из звездочек – результаты декорирования.
'''

# import datetime

# def prints_stars(func):
#     def wrapper():
#         print("***********************")
#         func()
#         print("***********************")

#     return wrapper

# def current_time():
#     print(datetime.datetime.now().strftime("%H:%M"))

# decorated_current_time = prints_stars(current_time)

# decorated_current_time()


'''
Добавьте ещё однуфункциюдля декорирования вывода
данных. Эта функция должна добавить новые элементы
в форматирование вывода.
'''
# import datetime

# def prints_stars(func):
#     def wrapper():
#         print("***********************")
#         func()
#         print("***********************")

#     return wrapper

# def prints_hash(func):
#     def wrapper():
#         print("###############################")
#         func()
#         print("###############################")

#     return wrapper

# def current_time():
#     print(datetime.datetime.now().strftime("%H:%M"))

# star_decorated = prints_stars(current_time)
# final_decorator = prints_hash(star_decorated)

# final_decorator()


'''
Решите задачу из первого задания с использованием
синтаксиса декораторов.
'''
# import datetime

# def prints_stars(func):
#     def wrapper():
#         print("***********************")
#         func()
#         print("***********************")
#     return wrapper

# def prints_hash(func):
#     def wrapper():
#         print("###############################")
#         func()
#         print("###############################")
#     return wrapper

# @prints_hash
# @prints_stars
# def current_time():
#     print(datetime.datetime.now().strftime("%H:%M"))

# current_time()


'''
Создайте приложение по выпечке пиццы. Каждая
пицца содержит разные компоненты. Используя механизм
декораторов создайте разные пиццы:
■ Маргарита;
■ Четыре сыра;
■ Капричоза;
■ Гавайская.
'''


# Базовая пицца
def pizza():
    return ['тесто', 'томатный соус', 'сыр']

# Декораторы пиццы
def margherita(func):
    def wrapper():
        result = func()
        result.append('томаты')
        result.append('базилик')
        return result
    return wrapper

def four_cheeses(func):
    def wrapper():
        result = func()
        result.extend(['моцарелла', 'горгонзола', 'дор блю', 'пармезан'])
        return result
    return wrapper

def capricciosa(func):
    def wrapper():
        result = func()
        result.extend(['ветчина', 'шампиньоны'])
        return result
    return wrapper

def hawaiian(func):
    def wrapper():
        result = func()
        result.extend(['ветчина', 'ананас'])
        return result
    return wrapper

# Создание пицц
@margherita
def margherita_pizza():
    return pizza()

@four_cheeses
def four_cheeses_pizza():
    return pizza()

@capricciosa
def capricciosa_pizza():
    return pizza()

@hawaiian
def hawaiian_pizza():
    return pizza()

print("Маргарита:", margherita_pizza())
print("Четыре сыра:", four_cheeses_pizza())
print("Капричоза:", capricciosa_pizza())
print("Гавайская:", hawaiian_pizza())
