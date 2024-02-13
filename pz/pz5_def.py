'''Напишите функцию, которая отображает на экран
форматированный текст, указанный ниже:
“Don't let the noise of others' opinions
drown out your own inner voice.”
Steve Jobs'''

'''Напишите функцию, которая принимает два числа
в качестве параметра и отображает все нечетные числа
между ними.'''
# def num(a,b):
#     for i in range(a,b):
#         if i  % 2 != 0:
#             print(i)

# num(20, 89)


'''Напишите функцию, которая отображает горизонтальную или вертикальную линию из некоторого символа.
Функция принимает в качестве параметра: длину линии,
направление, символ.'''
# line = 'вертикаль'
# width = 10
# symbol = '&'

# def line_func(line, width, symbol):
#     if line.lower() == 'горизонт':
#         print(symbol * width)
#     elif line.lower() == 'вертикаль':
#         while  width > 0:
#             print(symbol)
#             width -= 1
# line_func(line,width,symbol)


# size = 5
# cross = [[' ' for _ in range(size)] for _ in range(size)]
# print(cross)
# for i in range(size):
#     cross[i][i] = '*'
#     cross[i][size-i-1] = '*'

# for row in cross:
#     print(' '.join(row))
    # print('1')

'''Напишите функцию, которая возвращает максимальное из четырёх чисел. Числа передаются в качестве
параметров.'''
# def num(*args):
#     if len(args) == 4:
#         max_num = max(args)
#         return max_num
#     else:
#         print('Чисел много')
# v_func = num(22,23,54,462, 2)
# print(v_func)

'''Напишитефункцию, которая возвращает сумму чисел
в указанном диапазоне. Границы диапазона передаются
в качестве параметров.'''
# def  sum_of_numbers(start, end):
#     summ = 0
#     for i in  range(start,end+1):
#         summ += i
#     return summ

# result = sum_of_numbers(23, 98)
# print(result)

'''Напишите функцию, которая проверяет является ли
число простым. Число передаётся в качестве параметра.
Если число простое нужно вернуть из метода true, иначе
false'''

# def is_prime(n):
#     if n <= 1:
#         return False
#     elif n == 2:
#         return True
#     else:
#         for i in range(2, n):
#             if n % i == 0:
#                 return False
#         return True
# result = is_prime(7)
# print(result)


'''Написать игру «Крестики-нолики».'''

# def print_board(board):
#     for i in board:
#         print(' '.join(i))
#     # print("\n".join([" ".join(row) for row in board]))

# def check_win(board):
#     print(board)
#     for row in board:
#         if len(set(row)) == 1 and row[0] != " ":
#             return True
#     for i in range(3):
#         if (board[0][i] == board[1][i] == board[2][i]) and board[0][i] != " ":
#             return True
#     if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != " ":
#         return True
#     if (board[0][2] == board[1][1] == board[2][0]) and board[0][2] != " ":
#         return True
#     return False



# def play_game():
#     board = [[" " for _ in range(3)] for _ in range(3)]
#     current_player = "X"

#     while True:
#         print_board(board)
#         x = int(input(f"Игрок {current_player}, введите ряд (0-2): "))
#         y = int(input(f"Игрок {current_player}, введите столбец (0-2): "))
        
#         if board[x][y] != " ":
#             print("Неверный ход, место не пусто!")
#             continue
        
#         board[x][y] = current_player

#         if check_win(board):
#             print(f"Игрок {current_player} выйграл!")
#             break

#         current_player = "O" if current_player == "X" else "X"

# play_game()



'''БЫки и коровы'''
'''- Генерируется случайное четырехзначное число.
- Игрок вводит свое предположение о числе, и программа сравнивает его с сгенерированным числом.
- За каждую цифру, стоящую на правильном месте, игрок получает быка.
- За каждую цифру, присутствующую в числе, но стоящую на неправильном месте, игрок получает корову.
- Игра продолжается до тех пор, пока игрок не угадает все цифры и не получит 4 быка.'''
import random

def game():
    generated_number = str(random.randint(1000, 9999)) # Генерируем четырехзначное число
    print("Добро пожаловать в игру 'Быки и коровы'! Число уже выбрано, попробуйте его отгадать.")

    while True:
        user_number = input("Введите четырехзначное число: ")
        if len(user_number) != 4 or not user_number.isdigit():
            print("Ввод неверен. Пожалуйста, введите четырехзначное число.")
            continue

        bulls = 0
        cows = 0
        for i in range(4):
            if user_number[i] == generated_number[i]:
                bulls += 1
            elif user_number[i] in generated_number:
                cows += 1

        print(f"{bulls} бык(а/ов), {cows} коров(а/ы)")
        
        if bulls == 4:
            print("Поздравляем! Вы угадали число!")
            break

game()