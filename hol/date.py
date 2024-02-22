'''
Модуль datetime встроен в стандартную библиотеку Python. Для работы с датами и временем модуль предлагает специальные типы данных, например date, time и datetime.
'''

'''
Тип данных date
Тип данных date предназначен для работы с датами. В значениях этого типа можно хранить год, месяц и день. 
Как обьявить дату:
 - импортировать тип данных date из модуля datetime;
 - объявить переменную типа date, передав параметры через запятую: первым аргументом — год, вторым — месяц, третьим — день.
'''
# from datetime import date
# date_test = date(2024,2,22)
# print(date_test)


'''
Тип данных time
Для работы с секундами, минутами и часами применяют тип данных time. В переменную этого типа не получится записать ни год, ни месяц, ни день.
При описании переменной первым аргументом можно передать час, вторым минуту, третьим секунду. 
'''
# from datetime import time
# time_test = time(20, 35, 2)
# print(time_test)


'''
Тип данных datetime
Тип datetime позволяет сохранить дату и время как единое значение. Порядок аргументов: год, месяц, день, часы, минуты, секунды и микросекунды.
'''
# from datetime import datetime
# dete_time = datetime(2024, 2, 6, 9, 15, 0) 
# print(dete_time)

# d = datetime.date(dete_time)
# t = datetime.time(dete_time)
# print(d)
# print(t)


'''
С типами datetime, date можно выполнять арифметические операции вычитания, чтобы найти разницу во времени, а также можно сравнивать значения дат и времени.
'''
# from datetime import date, datetime

# day = date(2023, 11, 6)
# today = date(2023, 10, 12)
# print(day - today)

'''Чтобы вычислить точное время до дедлайна вплоть до секунд, надо применить значения типа datetime'''
# d_detail = datetime(2023, 11, 6, 9, 15, 00)
# today_detail = datetime(2023, 10, 12, 22, 13, 55)
# print(d_detail - today_detail)



'''Тип timedelta'''
'''
Разность значений типов date или datetime возвращает значение типа timedelta. Этот тип хранит не значение времени в настоящем, прошлом или будущем, а продолжительность некоего отрезка времени.

Разность дат возвращает длительность.
В программировании на Python есть типы данных для работы с датами и временем. Это может пригодиться, например, если нужно вычислить, сколько дней прошло между двумя событиями.
Представим, есть две даты - дата начала события и дата окончания события. Если вычесть одну дату из другой, то получите значение типа timedelta. Это значение не хранит конкретное время - оно показывает продолжительность отрезка времени между двумя датами.
Например, если одно событие началось 1 января, а другое - 10 января, то разность этих дат будет равна 9 дням. Это и есть значение типа timedelta.
Важно понимать, что timedelta не указывает конкретное время, а только продолжительность. Это может быть полезно в различных задачах, связанных с анализом временных интервалов.
'''
from datetime import datetime, timedelta
deadline_detail = datetime(2023, 11, 6, 9, 15, 00)
# today_detail = datetime(2023, 10, 12, 22, 13, 55)
print(deadline_detail)
# delta = deadline_detail - today_detail 

delta = timedelta(days=10)
print(deadline_detail + delta)

start = datetime(2023, 4, 1, 12, 0, 0)
end = datetime(2023, 4, 8, 12, 0, 0)
delta = end - start
print(delta.days) 
print(delta.seconds) 





'''Значения даты и времени можно сравнивать по тому же принципу, что и обычные числа, — посредством операторов сравнения <, >, ==. 
Логическая операция сравнения возвращает значение True или False:
'''
from datetime import datetime
deadline = datetime(2023, 11, 6, 13, 00, 00)
today = datetime(2023, 10, 12)
print(deadline > today)



'''Замена значения даты
Чтобы изменить дату, час, месяц, год или другие значения в данных типа datetime, используется replace():
'''
from datetime import datetime
datetime1 = datetime(2023, 8, 13, 3, 0, 0)  # 13 августа 2023 года, 3 утра
datetime2 = datetime.replace(datetime1, year=2019)  # 13 августа 2019 года, 3 утра
print('Исходная дата:', datetime1)
print('Изменённая дата:', datetime2)


'''Текущая дата и время'''
# При помощи now() получаем текущую дату и время.
# now = datetime.now()  
# При помощи today() получаем текущую дату.
# today_1 = datetime.today()
# today_2 = date.today()




'''
Форматирование времени
При выводе даты и времени на печать можно настроить свой формат. Для этого используется функция strftime(). Эта функция преобразует время в строку по заданному шаблону.
'''
from datetime import datetime

date_test = datetime(2023, 11, 6, 13, 0, 0)
# Синтаксис: datetime.strftime(<дата>, 'шаблон_для_форматирования')
deadline_as_str = datetime.strftime(date_test, '%Y/%m/%d %H:%M')
print(deadline_as_str)
# Выведется:
#  2023/11/06 13:00 
'''
Строка %Y/%m/%d %H:%M — это шаблон. Она состоит из условных обозначений и показывает, на каком месте в строке должен находиться тот или иной элемент времени. %Y — это год, %m — месяц, %d — день, %H — часы, %M — минуты. В шаблоне можно указать любые текстовые символы, например разделители / и . или обозначения ч., мин. и сек..
'''




'''Есть ещё одна функция для работы с форматом времени — strptime. Она позволяет выполнить обратную операцию: преобразовать строку в тип данных datetime по заданному формату.
'''
from datetime import datetime
# %Y - год, %m - месяц, %d - день, %H - часы, %M - минуты
# Сохраняем в переменную строку с датой в странном формате.
datetime_as_str = '14/08 2023 04-01'
# Составляем шаблон %d/%m %Y %H-%M 
# и преобразуем строку в значение типа datetime.
datetime_as_datetime = datetime.strptime(datetime_as_str, '%d/%m %Y %H-%M')
# Смотрим, что получилось:
print(datetime_as_datetime, type(datetime_as_datetime))











''''
from datetime import datetime, date

def timedelta_days(datetime_str_1, datetime_str_2):
    # Напишите тело функции.
    date1 = datetime.date(datetime.strptime(datetime_str_1, '%Y/%m/%d %H:%M:%S'))
    date2 = datetime.date(datetime.strptime(datetime_str_2, '%Y/%m/%d %H:%M:%S'))
    res = str(date2 - date1)
    return int(res[:4])

difference = timedelta_days('2019/05/10 00:00:00', '2019/10/04 00:00:00')

print('От начала посевной до начала сбора урожая прошло', difference, 'дней.')
'''