class User:
    """ Некий пользователь чего-то """

    __name: str = ''
    __age: int = 0

    def __init__(self) -> None:
        """ Конструктор объекта """

    # getter
    @property
    def name(self) -> str:
        return self.__name

    # setter, определяется только после getter
    @name.setter
    def name(self, name: str) -> None:
        if len(name) < 2:
            print('Имя должно быть не короче 2-х символов')
        else:
            self.__name = name

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int) -> None:
        if 6 < age < 120:
            self.__age = age
        else:
            print('Введите корректный возраст')


# MARK: использование класса

user1: User = User()
print(user1.age)
user1.name = 'Bob'
print(user1.name)
user1.age = 40
print(user1.age)

user1.name = 'X'
print(user1.name)