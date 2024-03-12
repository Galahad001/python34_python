# Декораторы для методов класса

```bash
class Robot:
    # Состояние батареи базовой станции:
    base_battery_status = 100

    def __init__(self, name):
        self.name = name

    def update_base_battery_status(self, new_status):
        """Обновляет состояние батареи базовой станции."""
        self.base_battery_status = new_status

    def report(self):
        """Печатает в консоли состояние батареи базовой станции."""
        print(
            f'{self.name} reporting: Battery status is '
            f'{self.base_battery_status}%'
        )


# Создаём двух роботов:
robot1 = Robot('R2-D2')
robot2 = Robot('C-3PO')

# Печатаем состояние батареи:
robot1.report()
robot2.report()

# Обновляем статус батареи - но только в одном из роботов:
robot1.update_base_battery_status(80)

# Снова печатаем состояние батареи:
robot1.report()
robot2.report() 
```

Декоратор @classmethod
По умолчанию все методы в классе привязаны к экземпляру класса, а не к самому классу. Однако с помощью декоратора @classmethod можно объявить метод, который привязан к классу, а не к его экземпляру.

Такие методы называют методами класса.

При объявлении методов класса первым параметром указывается cls. Этот параметр указывает на сам класс, а не на объект этого класса. Название cls — традиционно принятое: можно назвать его иначе, но лучше соблюдать традиции, так всем будет проще читать ваш код.
```bash
class Robot:
    # Состояние батареи базовой станции:
    base_battery_status = 100

    def __init__(self, name):
        self.name = name

    # Декорируем и изменяем метод update_base_battery_status(),
    # чтобы менять значение атрибута не в объекте, а в классе:
    @classmethod
    def update_base_battery_status(cls, new_status):  # Указываем аргумент cls.
        """Обновляет состояние батареи базовой станции."""
        # Присваиваем новое значение атрибуту класса.
        cls.base_battery_status = new_status

    def report(self):
        """Печатает в консоли состояние батареи базовой станции."""
        print(
            f'{self.name} reporting: Battery status is '
            f'{self.base_battery_status}%'
        )


# Создаём двух роботов:
robot1 = Robot('R2-D2')
robot2 = Robot('C-3PO')

# Печатаем состояние батареи:
robot1.report()
robot2.report()

# Обновляем статус батареи в классе: обращаемся не к объекту, а к классу.
Robot.update_base_battery_status(80)

# Снова печатаем состояние батареи:
robot1.report()
robot2.report()
```

Значение атрибута base_battery_status хранится на уровне класса. Метод update_base_battery_status() изменяет это значение в классе, а не в объекте.

Метод update_base_battery_status() доступен для любого объекта класса Robot, таким образом любому из объектов доступен метод для изменения атрибута base_battery_status и любой из объектов всегда будет «знать» актуальное значение этого атрибута.


# Статические методы класса
Статические методы в основном используются как вспомогательные функции и работают как обычные функции, обрабатывая данные, которые им переданы. Они описываются при помощи декоратора @staticmethod.

При объявлении статического метода в него не нужно передавать параметр, указывающий на объект или класс: не нужен ни self, ни cls. Статические методы никак не привязаны к классу или объекту, их можно воспринимать как методы, которые «не знают, к какому классу относятся».
```bash
class Robot:
    base_battery_status = 100

    def __init__(self, name):
        self.name = name

    @classmethod
    def update_base_battery_status(cls, new_status):
        cls.base_battery_status = new_status

    def report(self):
        print(
            f'{self.name} reporting: Battery status is '
            f'{self.base_battery_status}%'
        )

    @staticmethod
    def predict_battery_lifetime(current_capacity, charge_cycles):
        """
        Прогнозирует срок службы аккумулятора
        на основе текущей ёмкости и количества циклов зарядки.
        """
        # Пусть максимальная ёмкость нового аккумулятора будет равна 5000 мАч
        max_capacity = 5000
        return (current_capacity / max_capacity) * (1000 - charge_cycles)


# Вызов статического метода через имя класса:
battery_lifetime = Robot.predict_battery_lifetime(4000, 100)
print(
    'Прогноз срока службы аккумулятора: '
    f'осталось {battery_lifetime:.0f} циклов зарядки.'
)


# Создаём объект класса:
robot = Robot('R2-D2')
# Статический метод доступен и в объекте:
r2d2_battery_lifetime = robot.predict_battery_lifetime(3500, 150)
print(
    'Прогноз срока службы аккумулятора: '
    f'осталось {r2d2_battery_lifetime:.0f} циклов зарядки.'
) 
```


# Свойства объекта
Декоратор @property

Метод identifier() возвращает характеристику объекта — и обращаться к нему удобнее как к атрибуту. Для этого метод можно представить как свойство экземпляра класса.

Свойством экземпляра называется такой метод, работа с которым подобна работе с атрибутом.
Для определения метода как свойства применяют декоратор @property.
```bash
class Robot:
    base_battery_status = 100

    def __init__(self, name):
        self.name = name

    @classmethod
    def update_base_battery_status(cls, new_status):
        cls.base_battery_status = new_status

    def report(self):
        print(
            f'{self.name} reporting: Battery status is '
            f'{self.base_battery_status}%'
        )

    @staticmethod
    def predict_battery_lifetime(current_capacity, charge_cycles):
        """
        Прогнозирует срок службы аккумулятора
        на основе текущей ёмкости и количества циклов зарядки.
        """
        max_capacity = 5000
        return (current_capacity / max_capacity) * (1000 - charge_cycles)

    @property
    def identifier(self):
        """Вычисляет уникальный идентификатор робота на основе его имени."""
        # Преобразование имени в числовое представление:
        return sum(ord(char) for char in self.name)


# Создаём робота:
robot = Robot('R2-2')
print(robot.identifier)
```

Декоратор @classmethod используется для создания методов класса. Эти методы имеют доступ к самому классу через аргумент cls. Декоратор может использоваться для реализации методов, которым нужен доступ к классу, а не к конкретному экземпляру.

Декоратор @staticmethod позволяет определять в классе методы, которые не зависят от экземпляра (self) или класса (cls). При помощи этого декоратора удобно создавать вспомогательные функции, которые логически связаны с классом, но не требуют доступа к его атрибутам или методам.

Декоратор @property используется для создания свойств класса из методов.