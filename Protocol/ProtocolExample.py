from  typing import Protocol

class Quackable(Protocol):
    def quack(self) -> str: ...

class WildDuck():
    def quack(self) -> str:
        return "quack"

class Decoy():
    def quack(self) -> str:
        return "*False* quack"

class RubberDuck():
    def quack(self) -> str:
        return "squeak"


def action (value: Quackable) -> None:
    print(value.quack())

duck = WildDuck()
rubber_duck = RubberDuck()
decoy = Decoy()
action(duck)
action(rubber_duck)
action(decoy)
# action("asdf")