'''Запись в файл - способ сохранить данные даже после закрытия терминала с программой'''
'''Чтобы записать данные в файл, нужно вызвать open и помимо имени файла передать второй аргумент, он сообщает Питону что эти данные записываются в файл'''
f_name = 'test.txt'
# with open(f_name, 'w', encoding='utf-8') as file:
#     file.write('Этот скрипт работает')


# Присоединение данных
'''Для добавления новых дынных не удаляя предыдушие используется  режим  (a). Все строки добавятся в конец файла'''
# with open(f_name, 'a', encoding='utf-8') as file:
#     file.write('Добавим текст к существующему \n')
#     file.write('Пару раз\n')
