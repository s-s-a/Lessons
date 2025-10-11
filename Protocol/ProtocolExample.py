from typing import Protocol


class Quackable(Protocol):
    """ Квакабельный """

    def quack(self) -> str:
        """ Квакнуть """
        ...


class WildDuck:
    """ Дикая утка """
    def quack(self) -> str:
        """
        Квакание дикой утки
        :return:
        """
        return "quack"


class Decoy:
    """ Имитатор утки (манок)"""
    def quack(self) -> str:
        """
        Квакание имитатора утки
        :return:
        """
        return "*False* quack"


class RubberDuck:
    """ Резиновая утка """
    def quack(self) -> str:
        """
        Квакние резиновой утки
        :return:
        """
        return "squeak"


def action(value: Quackable) -> None:
    """
    Действие - квакать
    :param value:
    """
    print(value.quack())


duck = WildDuck()
rubber_duck = RubberDuck()
decoy = Decoy()
action(duck)
action(rubber_duck)
action(decoy)
# action("asdf")
