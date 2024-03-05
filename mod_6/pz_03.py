'''
Используя механизм множественного наследования
разработайте класс “Автомобиль”. Должны быть классы
«Колеса», «Двигатель», «Двери» и т.д
'''

# class Wheels:
#     def __init__(self):
#         self.num_of_wheels = 4

#     def display_wheels(self):
#         print(f"У машины {self.num_of_wheels} колеса.")

# class Engine:
#     def __init__(self):
#         self.power = 150

#     def display_engine(self):
#         print(f"Двигатель автомобиля имеет мощность {self.power} л.с.")

# class Doors:
#     def __init__(self):
#         self.num_of_doors = 4

#     def display_doors(self):
#         print(f"В этой машинеs {self.num_of_doors} двери.")

# # Car class with multiple inheritance
# class Car(Wheels, Engine, Doors):
#     def __init__(self, model):
#         Wheels.__init__(self)
#         Engine.__init__(self)
#         Doors.__init__(self)
#         self.model = model

#     def display_info(self):
#         print(f"This is a {self.model}.")
#         self.display_wheels()
#         self.display_engine()
#         self.display_doors()

# car = Car("Tesla Model S")
# car.display_info()



'''
Создать базовый класс «Домашнее животное» и производные классы«Собака», «Кошка», «Попугай», «Хомяк».
С помощью конструктора установить имя каждого животного и его характеристики. Реализуйте для каждого
из классов методы:
■ Sound — издает звук животного (пишем текстом в
консоль);
■ Show — отображает имя животного;
■ Type — отображает название его подвида;
'''
# class Pet:
#     def __init__(self, name, type_):
#         self.name = name
#         self.type = type_

#     def sound(self):
#         print(f"{self.name} издает звук.")

#     def show(self):
#         print(f"Имя животного: {self.name}")

#     def type2(self):
#         print(f"Тип: {self.type}")

# class Dog(Pet):
#     def __init__(self, name, breed):
#         super().__init__(name, 'Собака')
#         self.breed = breed

#     def sound(self):
#         print(f"{self.name} лает.")

# class Cat(Pet):
#     def __init__(self, name, breed):
#         super().__init__(name, 'Кошка')
#         self.breed = breed

#     def sound(self):
#         print(f"{self.name} мяукает.")

# class Parrot(Pet):
#     def __init__(self, name, color):
#         super().__init__(name, 'Попугай')
#         self.color = color

#     def sound(self):
#         print(f"{self.name} крики.")

# class Hamster(Pet):
#     def __init__(self, name, color):
#         super().__init__(name, 'Хомяк')
#         self.color = color

#     def sound(self):
#         print(f"{self.name} хз что делает.")


# dog = Dog("Било", "Бульдог")
# cat = Cat("Миро", "Шотлодская")
# parrot = Parrot("Робинзон", "Зеленый")
# hamster = Hamster("Верценгеторик", "Благородная седина")

# # Call their methods
# dog.sound()
# dog.show()
# dog.type2()
# print()

# cat.sound()
# cat.show()
# cat.type2()
# print()

# parrot.sound()
# parrot.show()
# parrot.type2()
# print()

# hamster.sound()
# hamster.show()
# hamster.type2()


'''
Создать базовый класс Employer (служащий) с функцией Print(). Она должна выводить информацию о служащем. В случае базового класса это может быть строка
Создайте от него три производных класса: President,
Manager, Worker. Переопределите функцию Print() для
вывода информации, соответствующей каждому типу
служащего.
'''
# class Employer:
#     def __init__(self, name):
#         self.name = name

#     def print(self):
#         print("This is Employ class")
        

# class President(Employer):
#     def __init__(self, name, country):
#         super().__init__(name)
#         self.country = country

#     def print(self):
#         print(f"Президент: {self.name}, Страна: {self.country}")


# class Manager(Employer):
#     def __init__(self, name, department):
#         super().__init__(name)
#         self.department = department

#     def print(self):
#         print(f"Менеджер: {self.name}, Отделение: {self.department}")


# class Worker(Employer):
#     def __init__(self, name, job_title):
#         super().__init__(name)
#         self.job_title = job_title

#     def print(self):
#         print(f"Рабочий: {self.name}, Должность: {self.job_title}")


# employer = Employer("Имя")
# president = President("Иванов И.И.", "Страна М")
# manager = Manager("Пилотов П.П.", "Департамент отделения Х")
# worker = Worker("Сливов С.С.", "Работает на компанию")

# employer.print()
# president.print()
# manager.print()
# worker.print()



class Employer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "This is Employ class"

    def __int__(self):
        return self.age


class President(Employer):
    def __init__(self, name, age, country):
        super().__init__(name, age)
        self.country = country

    def __str__(self):
        return f"Президент: {self.name}, Страна: {self.country}"


class Manager(Employer):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def __str__(self):
        return f"Менеджер: {self.name}, Отделение: {self.department}"


class Worker(Employer):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title

    def __str__(self):
        return f"Рабочий: {self.name}, Должность: {self.job_title}"


employer = Employer("Employer Name", 45)
president = President("Иванов И.И.", 55, "Страна М")
manager = Manager("Пилотов П.П.", 40, "Департамент отделения Х")
worker = Worker("Сливов С.С.", 50, "Работает на компанию")

# Выведем информацию о служащих, используя магический метод __str__
print(employer)
print(president)
print(manager)
print(worker)

# Выведем возраст служащих, используя магический метод __int__
print(int(employer))
print(int(president))
print(int(manager))
print(int(worker))


# Методы `__str__`и `__int__` - это специальные (или "магические") методы в Python, которыми обладают все классы. `__str__` вызывается, когда мы хотим представить наш объект в виде строки (например, когда мы передаем его функции `print()`), а `__int__` - когда мы хотим преобразовать наш объект в целочисленное значение.