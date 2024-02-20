'''Напишите информационную систему «Сотрудники».
Программа должна обеспечивать ввод данных, редактирование данных сотрудника, удаление сотрудника, поиск
сотрудника по фамилии, вывод информации обо всех
сотрудниках, указанного возраста, или фамилия которых
начинается на указанную букву. Организуйте возможность
сохранения найденной информации в файл. Также весь
список сотрудников сохраняется в файл (при выходе из
программы — автоматически, в процессе исполнения
программы — по команде пользователя). При старте
программы происходит загрузка списка сотрудников из
указанного пользователем файла.'''
import os
print('Программа "Сотрудники"')
file = input('Введите номер/имя файла - ')
try:
    with open(file,'r', encoding='utf-8') as f:
        data=f.readlines()
        print(data)
except FileNotFoundError:
    print('Такого файла не сущеcтвует. Программа создала этот файл. Он пуст')
    with open(file, 'w') as f:
        f.write('')


# ввод данных
def add(file, employee):
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{employee} \n')
        print('Сотрудкик добавлен')

# редактирование данных сотрудника
def edit(file):
    print('Введите  ID сотрудника для редактирования')
    id_edit = input('ID - ')
    with open(file, 'r', encoding='utf-8') as f:
        data = f.readlines()
        data2 = []
        for i in data:
            if i.find(id_edit) != -1:
                l = i.split(' ')
                print(l)
                old = input('Старое значение ')
                new = input('Новое ')
                for  j in range(len(l)):
                    if l[j] == old:
                        l[j] = new
                        r = ' '.join(l)
                        data2.append(r)
            else:
                data2.append(i)
        print(data2)

        with open(file, 'w', encoding='utf-8') as f:
            f.writelines(data2)
              
#edit(file)


# удаление сотрудника
def delete(file):
    ids = []
    with open(file,'r',encoding='utf-8') as f:
        w = 0
        lines = f.readlines()
        print(lines)
        id_edit = input('ID сотрудника которого хотите удалить - ')
        for line in lines:
            message = line.split(' ')
            print(line)
            print(f'Это {message}')
            for j in range(len(message)):
                if message[j] == id_edit:
                    print(1)
                    del lines[w]
                else:
                    print(2)
                    ids.append(line)
            w += 1

    print(ids)
delete(file)