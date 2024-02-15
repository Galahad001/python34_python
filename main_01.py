'''Большие обьемы игфомации могут хранитя в текстовых файлах. Может хранится все что угодно.
Работа с информацией в текстовом файле начниается с чтения данных в память.'''

'''Открываем файл, читаем и выводим'''
with open('pi.txt') as file:
    res = file.read()
    print(res)
'''Open() - открывает файил. В параметр передается имя открываемого файла. Open возвраащает обьет, придставляющий файл pi.txt. Питон сохранит обьект в переменной file'''
'''With - - закрывает файл после того как надобность в нем пропадет'''
'''После появления обьекта (file) применяем метод read()-он читает все содержимое файла и сохраняет его в переменной res'''

# Чтение по строкам
'''Если нужно обработать каждую строку. Найти конкретную информацию. Для последовательной проверки можно использлвать цикл for'''
'''Пустые строки появляются изза того что каждая строка в файле завершается невидимым символам новой строки. Команда print добавляет еще и свой символ новой строки получается два символа новой строки.'''
# f = 'pi.txt'
# with open(f) as file:
#     for i in file:
#         # print(i)
#         print(i.rstrip())



# Список строк по содержимомму файла
'''readlines() - читает каждую строку из файла и сохраняет ее в списке. Список сохраненный в переменной можно использоать за пределами блока With'''
# f = 'pi.txt'
# with open(f) as file:
#     spis = file.readlines()
# print(spis)
'''аргумент  'w' - говорит что файл открыт в режиме записи. Файлы можно открывать в режимах (r - чтение, w - записи, a - присоеденения). Режим записи автоматически создаст файл если его еще не существует. Также этот режим уничтожает старые данные и ставит новые'''