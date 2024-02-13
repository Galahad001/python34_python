'''
Функция — это именованный блок кода, который выполняет конкретную задачу, — программа в программе. Функции помогают организовать код в более мелкие, но при этом самодостаточные фрагменты.
Разработчик создаёт функцию в коде программы — объявляет функцию и описывает в ней те действия, которые она должна выполнять.
'''

'''
После того как функция объявлена, нужно написать тело функции — код, который функция должна выполнять. 
Тело функции отбивается четырьмя пробелами от начала строки: так Python понимает, где начинается и заканчивается тело функции. Если отступов не будет, то Python решит, что тела функции нет, — и сообщит об ошибке: если функция объявлена, у неё должно быть тело, хотя бы одна строчка.
'''

'''
После того как функция объявлена, нужно написать тело функции — код, который функция должна выполнять. 
Тело функции отбивается четырьмя пробелами от начала строки: так Python понимает, где начинается и заканчивается тело функции. Если отступов не будет, то Python решит, что тела функции нет, — и сообщит об ошибке: если функция объявлена, у неё должно быть тело, хотя бы одна строчка.

Значения для этих параметров передаются при вызове — их называют аргументами функции.
'''
'''
При вызове функции аргументы передаются в соответствии с порядком записи (тоже через запятую): первый аргумент передаётся в первый параметр, второй аргумент — во второй параметр.
'''

'''
При вызове функции action() значения передаются в параметры в соответствии с их позицией, в порядке перечисления: первый аргумент передаётся в первый параметр, второй аргумент — во второй параметр. 
Такие аргументы называются позиционными.
'''

'''
У инструкции return есть одно важное свойство: она не только возвращает результат, но и прерывает работу функции. Код, который следует за return, никогда не будет выполнен.
В функции может быть несколько инструкций return, но выполнится только одна из них — та, которая в ходе выполнения программы будет обработана первой. После этого функция прекратит работу, а оставшуюся часть кода функции Python проигнорирует.
'''