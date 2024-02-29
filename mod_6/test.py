# class Employee:
#     vacation_days = 28

#     def __init__(self, first_name, second_name, gender):
#         self.first_name = first_name
#         self.second_name = second_name
#         self.gender = gender
#         self.remaining_vacation_days = Employee.vacation_days
#         self._employee_id = self.__generate_employee_id()

#     def consume_vacation(self, days):
#         self.remaining_vacation_days -= days

#     def get_vacation_details(self):
#         return f'Остаток отпускных дней: {self.remaining_vacation_days}.'
    
#     def __generate_employee_id(self):
#         return self.first_name + self.second_name + self.gender


# class FullTimeEmployee(Employee):
#     def __init__(self, first_name, second_name, gender, __salary):
#         super().__init__(first_name, second_name, gender)
#         self.__salary = __salary
                  
#     def get_unpaid_vacation(self, start_date, days):
#         return f'Начало неоплачиваемого отпуска: {start_date}, продолжительность: {days} дней.'

#     def __get_vacation_salary(self):
#         return self.__salary * 0.8
    

# class PartTimeEmployee(Employee):
#     vacation_days = 14

#     def __init__(self, first_name, second_name, gender):
#         super().__init__(first_name, second_name, gender)
#         self.remaining_vacation_days = PartTimeEmployee.vacation_days


# # Пример использования:
# full_time_employee = FullTimeEmployee('Иван', 'Иванов', 'м', 50000)
# print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))

# part_time_employee = PartTimeEmployee('Анна', 'Петрова', 'ж')
# part_time_employee.consume_vacation(5)
# print(part_time_employee.get_vacation_details())
# print(part_time_employee.vacation_days)
# print(Employee.vacation_days)



# print(full_time_employee.first_name)
# print(full_time_employee.second_name)
# print(full_time_employee.gender)
# print(full_time_employee._employee_id)

# print(full_time_employee._FullTimeEmployee__salary)

# print(full_time_employee._FullTimeEmployee__get_vacation_salary())




# class Transport:
#     def __init__(self, power, color='red'):
#         self.power = power
#         self.color = color
    
#     def start(self):
#         print("Транспорт запущен")

#     def stop(self):
#         print("Транспорт остановлен")


# class Ground(Transport):
#     def __init__(self, power, color, number_of_doors):
#         self.number_of_doors = number_of_doors
#         super().__init__(power, color)


# test = Ground(100, 'green', 2)
# print(test.color)
# print(test.number_of_doors)
# test.start()
# test.stop()
class Transport:
    def __init__(self, power, color='red'):
        self.power = power
        self.color = color
    
    def start(self):
        print("Транспорт запущен")

    def stop(self):
        print("Транспорт остановлен")

    def __str__(self):
        return f'Транспорт со скорость {self.power} км/ч'


class Ground(Transport):
    def __init__(self, power, color, number_of_doors, name):
        self.number_of_doors = number_of_doors
        self.__name = name
        super().__init__(power, color)

    def start(self):
        print('Транспорт начал движение')


    def __str__(self):
        return f'Машина {self.color} цвета'

bmw = Ground(150, 'black', 4, 'Иванов И.И.')

print(bmw._Ground__name)