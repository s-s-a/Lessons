
class Player:
    """

    """
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self) -> str:
        """

        :return:
        """
        return f'{self.name} is age {self.age}'

    def get_height(self) -> str:
        """

        :return:
        """
        return f'{self.name} is {self.height} cm'

    def get_weight(self) -> str:
        """

        :return:
        """
        return f'{self.name} weighs {self.weight} kg'


if __name__ == '__main__':
    pl = Player('Ann', 25, 164, 52)

    print(pl.get_age())
    print(pl.get_height())
    print(pl.get_weight())
