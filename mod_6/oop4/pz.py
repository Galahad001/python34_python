'''К уже реализованному классу «Человек» добавьте
статический метод, который при вызове возвращает количество созданных объектов класса «Человек».'''

# class Human:
#     count_people = 0

#     def __init__(self, имя):
#         self.имя = имя
#         Human.count_people += 1

#     @staticmethod
#     def get_people():
#         return Human.count_people



# p1 = Human("Иван")
# p2 = Human("Мария")
# p3 = Human("Коля")


# print(Human.get_people())


'''Создать класс для подсчета площади геометрических фигур. Класс должен предоставлять функциональность для подсчета площади треугольника по разнымформулам, площади прямоугольника, площади квадрата, площади ромба. Методы класса для подсчета площади должны быть реализованыс помощью статических методов. Также класс должен считать количество подсчетов площади и возвращать это значение с помощью статического метода '''
# import math

# class Geometry:
#     _count_area_calculations = 0

#     @staticmethod
#     def area_of_triangle(base, height):
#         Geometry._count_area_calculations += 1
#         return 0.5 * base * height

#     @staticmethod
#     def area_of_rectangle(length, width):
#         Geometry._count_area_calculations += 1
#         return length * width

#     @staticmethod
#     def area_of_square(side):
#         Geometry._count_area_calculations += 1
#         return side * side

#     @staticmethod
#     def area_of_rhombus(diagonal1, diagonal2):
#         Geometry._count_area_calculations += 1
#         return 0.5 * diagonal1 * diagonal2

#     @staticmethod
#     def get_calculation_count():
#         return Geometry._count_area_calculations


'''Создайте класс для подсчета максимума из четырех
аргументов, минимума из четырех аргументов, среднеарифметического из четырех аргументов, факториала
аргумента. Функциональность необходимо реализовать
в виде статических методов'''
# class Calculator:
#     @staticmethod
#     def max_of_four(x1, x2, x3, x4):
#         return max(x1, x2, x3, x4)

#     @staticmethod
#     def min_of_four(x1, x2, x3, x4):
#         return min(x1, x2, x3, x4)

#     @staticmethod
#     def average_of_four(x1, x2, x3, x4):
#         return (x1 + x2 + x3 + x4) / 4

#     @staticmethod
#     def factorial_of_arg(x):
#         if x == 0:
#             return 1
#         else:
#             fact = 1
#             for i in range(1, x + 1):
#                 fact *= i
#             return fact

# max_value = Calculator.max_of_four(1, 2, 3, 4)
# print(max_value)

'''Создайте класс Библиотека. Класс предназначен для
хранения информации о библиотеке (название, адрес, количество книг и т.д.). Реализуйте необходимые для класса
методы. Используя перегрузку операторов реализуйте для
него следующие арифметические операции:
■ + добавляет к количеству книг указанное значение;
■ += добавляет к количеству книг указанное значение;
■ -= вычитает из количества книг указанное значение;
Используя перегрузку операторов реализуйте (сравнение по количеству книг):
■ <;
■ >;
■ <=;
■ >=;
■ ==;
■ !=

'''

class Library:
    def __init__(self, name, address, number_of_books):
        self.name = name
        self.address = address
        self.number_of_books = number_of_books

    def __str__(self):
        return f'Библиотека "{self.name}" находится по адресу: {self.address}. Количество книг: {self.number_of_books}.'

    def __add__(self, other):
        if isinstance(other, (int, float)):
            self.number_of_books += other
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __isub__(self, other):
        if isinstance(other, (int, float)):
            self.number_of_books -= other
        return self

    # Операторы сравнения
    def __lt__(self, other):
        if isinstance(other, Library):
            return self.number_of_books < other.number_of_books

    def __gt__(self, other):
        if isinstance(other, Library):
            return self.number_of_books > other.number_of_books

    def __le__(self, other):
        if isinstance(other, Library):
            return self.number_of_books <= other.number_of_books

    def __ge__(self, other):
        if isinstance(other, Library):
            return self.number_of_books >= other.number_of_books

    def __eq__(self, other):
        if isinstance(other, Library):
            return self.number_of_books == other.number_of_books

    def __ne__(self, other):
        if isinstance(other, Library):
            return self.number_of_books != other.number_of_books

my_library = Library("Моя Библиотека", "ул. Пушкина, дом Колотушкина", 1000)
print(my_library)  # Вывод: Библиотека "Моя Библиотека" находится по адресу: ул. Пушкина, дом Колотушкина. Количество книг: 1000.

my_library += 100
print(my_library)  # Вывод: Библиотека "Моя Библиотека" находится по адресу: ул. Пушкина, дом Колотушкина. Количество книг: 1100.

my_library -= 50
print(my_library)  # Вывод: Библиотека "Моя Библиотека" находится по адресу: ул. Пушкина, дом Колотушкина. Количество книг: 1050.


# my_library = Library("Моя Библиотека", "ул. Пушкина, дом Колотушкина", 1000)
# other_library = Library("Другая Библиотека", "ул. Лермонтова, дом Котов", 2000)

# # использование +=
# my_library += 50
# print(my_library)  # Библиотека "Моя Библиотека" находится по адресу: ул. Пушкина, дом Колотушкина. Количество книг: 1050.

# # использование -=
# my_library -= 40
# print(my_library)  # Библиотека "Моя Библиотека" находится по адресу: ул. Пушкина, дом Колотушкина. Количество книг: 1010.

# # использование операторов сравнения
# print(my_library < other_library)  # True
# print(my_library > other_library)  # False
# print(my_library <= other_library)  # True
# print(my_library >= other_library)  # False
# print(my_library == other_library)  # False
# print(my_library != other_library)  # True


# Функция isinstance() проверяет, является ли объект экземпляром указанного класса или его подкласса. Если требуется проверить, принадлежит ли объект к определенному классу или его подклассу, лучше использовать isinstance().