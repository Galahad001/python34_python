'''
Создайте класс Human, который будет содержать
информацию о человеке.
Спомощью механизма наследования, реализуйте класс
Builder (содержит информацию о строителе), класс Sailor
(содержит информацию о моряке), класс Pilot (содержит
информацию о летчике).
Каждый из классов должен содержать необходимые
для работы методы
'''
# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_info(self):
#         print(f"Имя: {self.name}")
#         print(f"Возраст: {self.age}")

# class Builder(Human):
#     def __init__(self, name, age, tools):
#         super().__init__(name, age)
#         self.tools = tools

#     def display_info(self):
#         super().display_info()
#         print(f"Инструменты: {', '.join(self.tools)}")

#     def build(self):
#         print(f"{self.name} строит что-то...")

# class Sailor(Human):
#     def __init__(self, name, age, ship_name):
#         super().__init__(name, age)
#         self.ship_name = ship_name

#     def display_info(self):
#         super().display_info()
#         print(f"Название корабля: {self.ship_name}")

#     def sail(self):
#         print(f"{self.name} плывет дальше {self.ship_name}...")

# class Pilot(Human):
#     def __init__(self, name, age, airplane_model):
#         super().__init__(name, age)
#         self.airplane_model = airplane_model

#     def display_info(self):
#         super().display_info()
#         print(f"Модель самолета: {self.airplane_model}")

#     def fly(self):
#         print(f"{self.name} летит дальше {self.airplane_model}...")

# # Создайте экземпляры классов Builder, Sailor и Pilot.
# bob = Builder("Боб", 33, ["молоток", "отвертка"])
# jack = Sailor("Джек", 29, "Черная Жемчужина")

# fitz = Pilot("Фиц", 39, "Боинг 747")

# #Отображать информацию и выполнять свою работу
# bob.display_info()
# bob.build()

# jack.display_info()
# jack.sail()

# fitz.display_info()
# fitz.fly()


'''
Создайте класс Passport (паспорт), который будет
содержать паспортную информацию о гражданине заданной страны.
С помощью механизма наследования, реализуйте
класс ForeignPassport (загран.паспорт) производный от
Passport.
Напомним, что заграничный паспорт содержит помимо паспортных данных, также данные о визах, номер
заграничного паспорта.
Каждый из классов должен содержать необходимые
методы.
'''

# class Passport:
#     def __init__(self, name, birthdate, passport_number, nationality):
#         self.name = name
#         self.birthdate = birthdate
#         self.passport_number = passport_number
#         self.nationality = nationality

#     def display_info(self):
#         print("Информация:")
#         print(f"Имя: {self.name}")
#         print(f"Дата рождения: {self.birthdate}")
#         print(f"Номер паспорта: {self.passport_number}")
#         print(f"Национальность: {self.nationality}")

# class ForeignPassport(Passport):
#     def __init__(self, name, birthdate, passport_number, nationality, foreign_passport_number, visas):
#         super().__init__(name, birthdate, passport_number, nationality)
#         self.foreign_passport_number = foreign_passport_number
#         self.visas = visas

#     def display_info(self):
#         print("Загран. паспорт информация:")
#         super().display_info()
#         print(f"Номер загран паспорта: {self.foreign_passport_number}")
#         print("Visas:")
#         for visa in self.visas:
#             print(f" - {visa}")


# john_passport = Passport("Джон", "1990-01-01", "12345678", "Российская Федерация")
# john_foreign_passport = ForeignPassport("Джон", "1990-01-01", "12345678", "Российская Федерация", "87654321", ["Schengen visa", "UK visa"])


# john_passport.display_info()
# print()
# john_foreign_passport.display_info()


'''
Создать базовый класс «Животное» и производные классы «Тигр», «Крокодил», «Кенгуру». С помощью конструктора установить имя каждого животного и его характеристики. Создайте для каждого класса необходимые методы и поля.
'''

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} ест.")

#     def sleep(self):
#         print(f"{self.name} спит.")

# class Tiger(Animal):
#     def __init__(self, name, speed):
#         super().__init__(name)
#         self.speed = speed

#     def run(self):
#         print(f"{self.name} бежит со скоростью {self.speed} км/ч.")

# class Crocodile(Animal):
#     def __init__(self, name, length):
#         super().__init__(name)
#         self.length = length

#     def swim(self):
#         print(f"{self.name} плавает. Его {self.length} метров в длину.")

# class Kangaroo(Animal):
#     def __init__(self, name, leap_distance):
#         super().__init__(name)
#         self.leap_distance = leap_distance

#     def leap(self):
#         print(f"{self.name} прыгает на расстояние {self.leap_distance} метров.")

# # Instantiate the Animal, Tiger, Crocodile and Kangaroo classes
# tiger = Tiger("Тигр", 60)
# crocodile = Crocodile("Крокодил", 5)
# kangaroo = Kangaroo("Кенгуру", 9)

# # Call their methods
# tiger.eat()
# tiger.sleep()
# tiger.run()
# print()

# crocodile.eat()
# crocodile.sleep()
# crocodile.swim()
# print()

# kangaroo.eat()
# kangaroo.sleep()
# kangaroo.leap()


'''
Создать базовый класс «Домашнее животное» и производные классы«Собака», «Кошка», «Попугай», «Хомяк».
С помощью конструктора установить имя каждого животного и его характеристики. Реализуйте для каждого
из классов методы:
■ Sound — издает звук животного (пишем текстом в
консоль);
■ Show — отображает имя животного;
■ Type — отображает название его подвида;
'''
class Pet:
    def __init__(self, name, type_):
        self.name = name
        self.type = type_

    def sound(self):
        print(f"{self.name} издает звук.")

    def show(self):
        print(f"Имя животного: {self.name}")

    def type2(self):
        print(f"Тип: {self.type}")

class Dog(Pet):
    def __init__(self, name, breed):
        super().__init__(name, 'Собака')
        self.breed = breed

    def sound(self):
        print(f"{self.name} лает.")

class Cat(Pet):
    def __init__(self, name, breed):
        super().__init__(name, 'Кошка')
        self.breed = breed

    def sound(self):
        print(f"{self.name} мяукает.")

class Parrot(Pet):
    def __init__(self, name, color):
        super().__init__(name, 'Попугай')
        self.color = color

    def sound(self):
        print(f"{self.name} крики.")

class Hamster(Pet):
    def __init__(self, name, color):
        super().__init__(name, 'Хомяк')
        self.color = color

    def sound(self):
        print(f"{self.name} хз что делает.")

# Create instances of Dog, Cat, Parrot, and Hamster classes
dog = Dog("Било", "Бульдог")
cat = Cat("Миро", "Шотлодская")
parrot = Parrot("Робинзон", "Зеленый")
hamster = Hamster("Верценгеторик", "Благородная седина")

# Call their methods
dog.sound()
dog.show()
dog.type2()
print()

cat.sound()
cat.show()
cat.type2()
print()

parrot.sound()
parrot.show()
parrot.type2()
print()

hamster.sound()
hamster.show()
hamster.type2()