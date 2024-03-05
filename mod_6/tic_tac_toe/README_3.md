Дополнить код игры возможностью вводить координаты ячейки для хода. Координаты — это номер строки и номер столбца. После того как координаты будут введены, они должны быть переданы в метод

```bash
# game.py

from gameparts import Board

def main():
    game = Board()
    game.display()
    # Тут пользователь вводит координаты ячейки.
    row = int(input('Введите номер строки: '))
    column = int(input('Введите номер столбца: '))
    # В метод make_move передаются те координаты, которые ввёл пользователь.
    game.make_move(row, column, 'X')
    print('Ход сделан!')
    game.display()

if __name__ == '__main__':
    main()
```

Когда вы вводите координаты для хода, вы вводите значения, которые потом используются как индекс для доступа к определённому элементу списка. Если в списке не окажется элемента с указанным индексом, то Python не поймёт, как ему действовать в такой ситуации, и «выбросит» исключение.


Помимо использования стандартных исключений, можно  создавать собственные. Для этого нужно создать новый класс, унаследованный от встроенного класса Exception.

Собственные исключения могут понадобиться, когда нужно создать более информативное сообщение об ошибке, чем стандартное сообщение Python. Ещё такие исключения пригодятся для особых ситуаций, которые не попадают под стандартные исключения. 

# Собственное исключение
1. Создать новый класс, который наследуется от встроенного класса Exception или его подклассов. Имя класса придумывает разработчик, но оно должно заканчиваться словом Error.
2. Переопределить метод __str__(). В нём можно понятным языком описать, что учитывает конкретное исключение.

В директории gameparts/ создайте файл exceptions.py и добавьте в него код собственного исключения с именем FieldIndexError. Это исключение будет унаследовано от подкласса IndexError.

```bash
# gameparts/exceptions.py

class FieldIndexError(IndexError):

    def __str__(self):
        return 'Введено значение за границами игрового поля' 
```


Чтобы воспользоваться исключением, его необходимо «выбросить» в нужный момент. Для этого используется ключевое слово raise, за которым следует класс исключения, встроенного или пользовательского.

```bash
# game.py

from gameparts import Board
# Из файла exceptions.py, который лежит в пакете gameparts,
# импортируется класс FieldIndexError.
from gameparts.exceptions import FieldIndexError

def main():
    game = Board()
    game.display()
    # Пользователь вводит номер строки.
    row = int(input('Введите номер строки: '))
    # Если введённое значение меньше нуля или больше или равно
    # field_size (это значение равно трём, оно хранится в модуле
    # parts.py)...
    if row < 0 or row >= game.field_size:
        # ...выбросить исключение FieldIndexError.
        raise FieldIndexError
    column = int(input('Введите номер столбца: '))
    if column < 0 or column >= game.field_size:
        raise FieldIndexError
    game.make_move(row, column, 'X')
    print('Ход сделан!')
    game.display()

if __name__ == '__main__':
    main()
```


Чтобы обработать ситуацию, когда пользователь вводит некорректные координаты ячейки, вам понадобится бесконечный цикл while. Он будет работать до тех пор, пока пользователь не введёт корректные значения координат игрового поля. Как только нужные значения будут введены, цикл завершится, и программа продолжит свою работу.

```bash
from gameparts import Board
from gameparts.exceptions import FieldIndexError


def main():
    game = Board()
    game.display()

    # Запускается бесконечный цикл.
    while True:
        # В этом блоке содержатся операции, которые могут вызвать исключение.
        try:
            # Пользователь вводит значение номера строки.
            row = int(input('Введите номер строки: '))
            # Если введённое число меньше 0 или больше
            # или равно game.field_size...
            if row < 0 or row >= game.field_size:
                # ...выбрасывается собственное исключение FieldIndexError.
                raise FieldIndexError
            column = int(input('Введите номер столбца: '))
            # Если введённое число меньше 0 или больше
            # или равно game.field_size...
            if column < 0 or column >= game.field_size:
                # ...выбрасывается собственное исключение FieldIndexError.
                raise FieldIndexError
        # Если возникает исключение FieldIndexError...
        except FieldIndexError:
            # ...выводятся сообщения...
            print(
                'Значение должно быть неотрицательным и меньше '
                f'{game.field_size}.'
            )
            print('Пожалуйста, введите значения для строки и столбца заново.')
            # ...и цикл начинает свою работу сначала,
            # предоставляя пользователю ещё одну попытку ввести данные.
            continue
        except ValueError:
            print('Буквы вводить нельзя. Только числа.')
            print('Пожалуйста, введите значения для строки и столбца заново.')
            continue
        except Exception as e:
            print(f'Возникла ошибка: {e}')
        # Если в блоке try исключения не возникло...
        else:
            # ...значит, введённые значения прошли все проверки
            # и могут быть использованы в дальнейшем.
            # Цикл прерывается.
            break

    game.make_move(row, column, 'X')
    print('Ход сделан!')
    game.display()


if __name__ == '__main__':
    main() 
```



----------------------


Чтобы реализовать логику смены игрока, нужно доработать код в файле game.py следующим образом:
1. Добавить переменную, в которой по умолчанию будет храниться значение X, так как в игре «Крестики-нолики» первый ход обычно делают крестиками. 
2. Добавить флаговую переменную running со значением по умолчанию True. Она понадобится для управления основным циклом игры. Пока поднят флаг (running = True) — игра продолжается. Если флаг опущен (running = False) — цикл останавливается, и игра заканчивается.
3. Реализовать смену игроков. Эта возможность должна работать следующим образом: в каждой новой итерации цикла, если current_player равен X, новым значением будет O, иначе — новым значением будет X. Для реализации такого описания подойдёт тернарный оператор: current_player = 'O' if current_player == 'X' else 'X'.

```bash
from gameparts import Board
from gameparts.exceptions import FieldIndexError


def main():
    game = Board()
    # Первыми ходят крестики.
    current_player = 'X'
    # Это флаговая переменная. По умолчанию игра запущена и продолжается.
    running = True
    game.display()

    # Тут запускается основной цикл игры.
    while running:

        print(f'Ход делают {current_player}')

        # Запускается бесконечный цикл.
        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Введите значения для строки и столбца заново.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Введите значения для строки и столбца заново.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break

        # Теперь для установки значения на поле само значение берётся
        # из переменной current_player.
        game.make_move(row, column, current_player)
        game.display()
        # Тернарный оператор, через который реализована смена игроков.
        # Если current_player равен X, то новым значением будет O,
        # иначе — новым значением будет X.
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main() 
```

Создать исключение для попытки повторного использования ячейки
```bash
class CellOccupiedError(Exception):

    def __str__(self):
        return 'Попытка изменить занятую ячейку' 
```


```bash
from gameparts import Board
# Добавился ещё один импорт - исключение CellOccupiedError.
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()

    while running:

        print(f'Ход делают {current_player}')

        # Запускается бесконечный цикл.
        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    # Вот тут выбрасывается новое исключение.
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Введите значения для строки и столбца заново.')
                continue
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Введите значения для строки и столбца заново.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break

        game.make_move(row, column, current_player)
        game.display()
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main() 
```

# Победа, пройгрыш, ничья

Чтобы определить ничью в игре, в класс в файле moduls.py нужно добавить метод с вложенным циклом, который будет искать свободные ячейки. Если они есть, то игра продолжится, а если нет — завершится.

```bash
 def is_board_full(self):
        # Цикл проходится по всем столбцам игрового поля.
        for i in range(self.field_size):
            # А потом по всем строчкам.
            for j in range(self.field_size):
                # Если находит свободную ячейку...
                if self.board[i][j] == ' ':
                    # ...игра продолжается.
                    return False
        # Иначе - ничья!
        return True
```

Чтобы программа могла определить победу, нужно:
1. Реализовать проверку по вертикали и горизонтали с помощью цикла. Он будет проходиться по каждой строке и столбцу и проверять, одинаковые ли в них символы.
2. Реализовать проверку по диагонали с помощью условия. Нужно сравнить символы в определённых позициях поля. Например, для главной диагонали — это [0][0], [1][1], [2][2], а для побочной — [0][2], [1][1], [2][0].
3.  основном цикле игры после каждого хода нужно запускать обе проверки и если хотя бы одна из них закончится успешно, то опускать флаг running и выводить результат игры в терминал.

```bash
    # Этот метод будет определять победу.
    def check_win(self, player):
        # Тут реализована проверка по вертикали и горизонтали.
        for i in range(3):
            if (all([self.board[i][j] == player for j in range(3)]) or
                    all([self.board[j][i] == player for j in range(3)])):
                return True
        # Тут реализована проверка по диагонали.
        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] == player
            or
            self.board[0][2] == self.board[1][1] == self.board[2][0] == player
        ):
            return True

        return False 
```

Доработать исполняющий код
```bash
from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError

def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()

    while running:

        print(f'Ход делают {current_player}')

        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Введите значения для строки и столбца заново.')
                continue
            except CellOccupiedError:
                print('Ячейка занята.')
                print('Пожалуйста, введите другие координаты.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Введите значения для строки и столбца заново.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break

        game.make_move(row, column, current_player)
        game.display()
        # После каждого хода надо делать проверку на победу и на ничью.
        if game.check_win(current_player):
            print(f'Победили {current_player}!')
            running = False
        elif game.is_board_full():
            print('Ничья!')
            running = False

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == '__main__':
    main() 
```