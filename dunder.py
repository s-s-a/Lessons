"""
Dunder методы, их имена начинаются и заканчиваются двойным подчеркиванием

__init__ по умолчанию не ждёт аргументы
__repr__ для прогеров, возвращает строку, по которой видно и можно воссоздать состояние объекта
__str__ для людей, возвращает строку для удобного чтения людьми. По умолчанию возвращает результат __repr__
__lt__, __gt__, __le__, __qe__ - методы сравнения
__contains__ - определяет вхождение в коллекцию
__bool__ по умолчанию True
"""


class Banknote:
    """
    Банкнота
    """

    def __init__(self, value: int):
        self.value = value

    def __repr__(self) -> str:
        return f'Banknote({self.value})'

    def __str__(self) -> str:
        return f'Банкнота номиналом {self.value} рублей'

    def __eq__(self, other) -> bool:
        # if other is None or not isinstance(other, Banknote):
        #     return False
        return self.value == other.value if not (other is None or not isinstance(other, Banknote)) else False

    def __lt__(self, other) -> bool:
        return self.value < other.value if not (other is None or not isinstance(other, Banknote)) else False

    def __gt__(self, other) -> bool:
        return self.value > other.value if not (other is None or not isinstance(other, Banknote)) else False

    def __le__(self, other) -> bool:
        return self.value <= other.value if not (other is None or not isinstance(other, Banknote)) else False

    def __ge__(self, other):
        return self.value >= other.value if not (other is None or not isinstance(other, Banknote)) else False


# class Iterator:
#     def __init__(self, container):
#         self.container = container
#         self.index = 0
#
#     def __next__(self):
#         while 0 <= self.index < len(self.container):
#             value = self.container[self.index]
#             self.index += 1
#             return value
#         raise StopIteration


class Wallet:
    """
    Кошелёк
    """
    def __init__(self, *banknotes: Banknote):
        self.container: list = []
        self.container.extend(banknotes)
        self.index = 0

    def __repr__(self):
        return f'Wallet({self.container})'

    def __contains__(self, item):
        return item in self.container

    def __bool__(self):
        return len(self.container) > 0

    def __len__(self) -> int:
        return len(self.container)

    def __call__(self, *args, **kwargs):
        return f'{sum(e.value for e in self.container)} рублей'

    # def __iter__(self):
    #     return Iterator(self.container)

    def __getitem__(self, item: int):
        if not (0 <= item < len(self.container)):
            raise IndexError
        return self.container[item]

    def __setitem__(self, key: int, value: Banknote):
        if not (0 <= key < len(self.container)):
            raise IndexError
        self.container[key] = value


if __name__ == '__main__':
    banknote = Banknote(50)
    fifty = Banknote(50)
    hundred = Banknote(100)
    wallet = Wallet(fifty, hundred, hundred)
    print(Banknote(500) in wallet)
    print(len(wallet))
    wallet[0] = Banknote(500)
    print(wallet[2])
    for money in wallet:
        print(money)
