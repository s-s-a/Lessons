# %%[markdown]
# Python - один из самых широко используемых языков программирования в мире. Однако из-за его простоты, позволяющей быстро сделать что-то, 
# он остаётся также одним из самых недооценённых.
# Если загуглить лучшие 10 продвинутых хитростей Python, то вы найдёте кучу постов или статей на LinkedIn с обзором тривиальных (но всё же 
# полезных) вещей типа генераторов или кортежей.

# Я пишу на Python уже двенадцать лет, и за это время нашёл кучу очень интересных, недооценённых, уникальных или (как может кто-то сказать) 
# "не-pythonic" хитростей, позволяющих по-настоящему расширить границы возможного для Python.
# Именно поэтому я решил собрать список из 14 лучших таких фич с примерами и дополнительными ресурсами на случай, если вы захотите изучить 
# их глубже.
# %% [markdown]
# 1. Перегрузка типизации
# %% [markdown]
# @overload - это декоратор из модуля typing Python, позволяющий определять множественные сигнатуры для одной функции. Каждая перегрузка 
# сообщает модулю контроля типов, какие конкретно ожидать передаваемые параметры.
# %% [markdown]
# Например, показанный ниже код указывает, что если mode=split, то возвращаться может только list[str], а если mode=upper, то может 
# возвращаться только str. (Кроме того, тип Literal ограничивает значения mode или split, или upper.)

# %% [python]
from typing import Literal, overload

@overload
def transform(data: str, mode: Literal["split"]) -> list[str]:
    ...

@overload
def transform(data: str, mode: Literal["upper"]) -> str:
    ...

def transform(data: str, mode: Literal["split", "upper"]) -> list[str] | str:
    if mode == "split":
        return data.split()
    else:
        return data.upper()

split_words = transform("hello world", "split")  # Возвращаемый тип list[str]
split_words[0]  # Модуль проверки типов доволен

upper_words = transform("hello world", "upper")  # Возвращаемый тип str
upper_words.lower()  # Модуль проверки типов доволен

upper_words.append("!")  # Невозможно получить доступ к атрибуту "append" для "str"

# %% [markdown]
# Перегрузки не только могут менять возвращаемый тип в зависимости от аргументов, но и способны гораздо на большее! В ещё одном примере мы 
# используем перегрузки типизации, чтобы передавался ИЛИ id, ИЛИ username, но не оба.

# %% [python]
@overload
def get_user(id: int = ..., username: None = None) -> User:
    ...

@overload
def get_user(id: None = None, username: str = ...) -> User:
    ...

def get_user(id: int | None = None, username: str | None = None) -> User:
    ...

get_user(id=1)  # Работает!
get_user(username="John")  # Работает!
get_user(id=1, username="John")  # Ни одна из перегрузок "get_user" не соответствует переданным аргументам

# %% [markdown]
# ... — это особое значение, часто используемое в перегрузках, чтобы обозначить, что параметр опциональный, но всё равно требует значения.
# %% [markdown]
# Бонусная хитрость: как вы, вероятно, знаете, Python также поддерживает строковые литералы. Они позволяют утверждать, что параметру могут 
# быть переданы только конкретные значения строк, что обеспечивает ещё большую безопасность типов. Можно воспринимать их, как легковесную 
# разновидность Enum!

# %% [python]

def set_color(color: Literal["red", "blue", "green"]) -> None:
    ...

set_color("red")
set_color("blue")
set_color("green")
set_color("fuchsia")  # Аргумент типа "Literal['fuchsia']" не может быть присвоен параметру "color"

# %% [markdown]
# ▍ Дополнительные ресурсы
# %% [markdown]
# * Python Type Hints: How to use @overload
# * PEP 3124 — Overloading, Generic Functions, Interfaces, and Adaptation
# * Python Docs — Overloads
# * PEP 586 — Literal Types
# %% [markdown]
# 2. Только именованные и только позиционные аргументы
# %% [markdown]
# По умолчанию и обязательные, и опциональные параметры можно присваивать синтаксисом и именованных, и позиционных аргументов. 
# Но что, если вам не нужно, чтобы это происходило? Этим позволяют управлять только именованные и только позиционные аргументы.

# %% [python]
def foo(a, b, /, c, d, *, e, f):
	#         ^        ^
	# Видели такое раньше?
	...

# %% [markdown]
# * отмечает параметры, которые могут быть только именованными. Аргументы после * должны передаваться только как 
# именованные аргументы.

# %% [python]

#   KW+POS | KW ONLY
#       vv | vv
def foo(a, *, b):
    ...

# == РАЗРЕШЕНО ==
foo(a=1, b=2)  # Все именованные
foo(1, b=2)  # Половина позиционных, половина именованных

# == ЗАПРЕЩЕНО ==
foo(1, 2)  # Нельзя использовать позиционный параметр вместо именованного
#      ^

# %% [markdown]
# / отмечает параметры, которые могут быть только позиционными. Аргументы перед / должны передаваться позиционно и 
# не могут использоваться, как именованные.

# %% [python]

# POS ONLY | KW POS
#       vv | vv
def bar(a, /, b):
    ...

# == РАЗРЕШЕНО ==
bar(1, 2)  # Все позиционные
bar(1, b=2)  # Половина позиционных, половина именованных

# == ЗАПРЕЩЕНО ==
bar(a=1, b=2)  # Нельзя использовать именованный параметр вместо позиционного
#   ^

# %% [markdown]
# Только именованные и только позиционные аргументы особенно полезны для разработчиков API, они позволяют ограничить 
# возможности использования и передачи аргументов.

# %% [markdown]
# ▍ Дополнительные ресурсы
# %% [markdown]
# * Using Positional-Only And Keyword-Only Arguments in Python
# * Stack Overflow: Why use positional-only parameters in Python 3.8+?
# * PEP 3102 – Keyword-Only Arguments
# * PEP 570 – Python Positional-Only Parameters
# %% [markdown]
# 3. Future-аннотации
# %% [markdown]
# Краткий урок истории типизации Python:
# %% [markdown]
# Это, скорее, не фича Python, а урок истории о системе типов Python и предназначении from __future__ import annotations 
# на случай, если это встретится вам в коде продакшена.
# %% [markdown]
# Изначально система типов Python появилась, как хак. Синтаксис сигнатур функций был введён в PEP 3107 Python 3.0 просто 
# как дополнительный способ декорирования функций, не имеющий функциональности контроля типов.
# %% [markdown]
# Настоящие спецификации сигнатур типов были добавлены позже, в Python 3.5 с PEP 484, но они были предназначены для 
# вычисления во время определения/привязки. Это отлично работало в простых случаях, но вызывало всё больше головной боли 
# с одним типом проблем: прямыми ссылками.
# %% [markdown]
# Из-за этого прямые ссылки (использование типа до момента его определения) требовали отката к применению строковых 
# литералов, снижая изящество кода и повышая возможность ошибок.

# %% [python]
# Это не сработает
class Foo:
    def action(self) -> Foo:
        # Возвращаемая сигнатура `-> Foo` вычисляется непосредственно во время определения,
        # но класс `Foo` на этом этапе ещё полностью не определён,
        # вызывая NameError в процессе контроля типов.
        ...

# Это обходное решение -> использование строковых типов
class Bar:
    def action(self) -> "Bar":
        # Обходное решение со строковыми литералами: некрасиво и повышает вероятность ошибок
        ...

# %% [markdown]
# PEP 563: Postponed Evaluation of Annotations было нацелено на устранение этой проблемы изменением времени вычисления 
# сигнатур типов. Вместо того, чтобы вычислять сигнатуры во время определения, PEP 563 выполняет внутреннее 
# преобразование типов в строки и откладывает вычисление до момента, когда они понадобятся, обычно во время статического 
# анализа. Это обеспечивает более чистые прямые ссылки без определения строковых литералов в явном виде и снижает оверхед 
# сигнатур типов в среде исполнения.

# %% [python]
from __future__ import annotations

class Foo:
    def bar(self) -> Foo:  # Теперь работает!
        ...

# %% [markdown]
# Так в чём же проблема?
# Для модулей контроля типов это изменение по большей мере остаётся прозрачным. Но поскольку PEP 563 реализует его, по сути, внутренне обращаясь со всеми типами, как со строками, то все, кто полагается на доступ к возвращаемым типам в среде исполнения (например, ORM, библиотеки сериализации, валидаторы, инъекторы зависимостей и так далее) будут иметь проблемы совместимости с этой новой системой.
# %% [markdown]
# Именно поэтому даже спустя десять лет после появления PEP современный Python (3.13 на момент написания моего поста) по-прежнему полагается на ту же хак-систему типов, внедрённую в Python 3.5.
# %% [python]

# ===== Обычная типизация Python =====
def foobar() -> int:
    return 1

ret_type = foobar.__annotations__.get("return")
ret_type
# Возвращает: <class 'int'>
new_int = ret_type()

# ===== С отложенным вычислением =====
from __future__ import annotations

def foobar() -> int:
    return 1

ret_type = foobar.__annotations__.get("return")
ret_type
# "int" (str)
new_int = ret_type()  # TypeError: 'str' object is not callable

# %% [markdown]
# В недавно появившемся PEP 649 предложен новый способ обработки сигнатур функций и классов Python при помощи отложенного, или «ленивого» вычисления. Вместо того, чтобы вычислять сигнатуры во время определения функции или класса, как это делалось традиционно, этот способ откладывает их вычисление до момента доступа к ним.
# %% [markdown]
# Это реализуется компиляцией выражений сигнатур в отдельную функцию, хранящуюся в специальном атрибуте __annotate__. При первой операции доступа к атрибуту __annotations__ эта функция вызывается для вычисления и кэширования сигнатур, делая их доступными для последующего доступа.
# %% [python]

# Пример кода из PEP 649

class function:
    # __annotations__ для объекта функции — это уже
    # "data descriptor" в Python, мы просто меняем то,
    # что он делает
    @property
    def __annotations__(self):
        return self.__annotate__()

# ...

def annotate_foo():
    return {'x': int, 'y': MyType, 'return': float}

def foo(x = 3, y = "abc"):
    ...

foo.__annotate__ = annotate_foo

class MyType:
   ...

foo_y_annotation = foo.__annotations__['y']

# %% [markdown]
# Эта стратегия отложенного вычисления решает такие проблемы, как прямые ссылки и циклические зависимости, потому что сигнатуры вычисляются только когда необходимы. Более того, это повышает производительность благодаря тому, что мы избегаем незамедлительного вычисления сигнатур, которые могут и не использоваться, сохраняя при этом полную семантическую информацию, поддерживающую инструменты интроспекции и контроля типов в среде исполнения.
# %% [markdown]
# Дополнительный факт: с версии 3.11 Python поддерживает тип Self (PEP 673), позволяющий правильно типизировать методы, возвращающие экземпляры своего собственного класса, решая эту конкретную проблему возвращаемых типов, ссылающихся на самих себя.

from typing import Self

class Foo:
    def bar(self) -> Self:
        ...
# %% [markdown]
# ▍ Дополнительные ресурсы
# %% [markdown]
# * A History Of Annotations
# * Python, Type Hints, and Future Annotations
# * __future__ — Future Statement Definitions
# * PEP 484 — Type Hints
# * PEP 563 — Postponed Evaluation of Annotations
# * PEP 649 — Deferred Evaluation Of Annotations Using Descriptors
# * PEP 749 — Implementing PEP 649
# %% [markdown]
# 4. Дженерики
# %% [markdown]
# А вы знали, что в Python есть дженерики? На самом деле, в Python 3.12 появился новый, более изящный синтаксис дженериков.
# %% [python]

class KVStore[K: str | int, V]:
    def __init__(self) -> None:
        self.store: dict[K, V] = {}

    def get(self, key: K) -> V:
        return self.store[key]

    def set(self, key: K, value: V) -> None:
        self.store[key] = value

kv = KVStore[str, int]()
kv.set("one", 1)
kv.set("two", 2)
kv.set("three", 3)
# %% [markdown]
# Изначально в Python 3.5 дженерики были реализованы при помощи синтаксиса TypeVar. Однако PEP 695 для Python 3.12 преобразовал сигнатуры типов с нативным синтаксисом для дженериков, псевдонимов типов и так далее.
# %% [python]

# СТАРЫЙ СИНТАКСИС — Python с 3.5 по 3.11
from typing import Generic, TypeVar

UnBounded = TypeVar("UnBounded")
Bounded = TypeVar("Bounded", bound=int)
Constrained = TypeVar("Constrained", int, float)

class Foo(Generic[UnBounded, Bounded, Constrained]):
    def __init__(self, x: UnBounded, y: Bounded, z: Constrained) -> None:
        self.x = x
        self.y = y
        self.z = z
# %% [python]

# НОВЫЙ СИНТАКСИС - Python 3.12+
class Foo[UnBounded, Bounded: int, Constrained: int | float]:
    def __init__(self, x: UnBounded, y: Bounded, z: Constrained) -> None:
        self.x = x
        self.y = y
        self.z = z
# %% [markdown]
# С этим изменением также была внедрена более мощная версия дженериков с переменным количеством аргументов (variadic generics). Благодаря ей можно создавать произвольное количество параметров типов для сложных структур данных и операций.
# %% [python]

class Tuple[*Ts]:
    def __init__(self, *args: *Ts) -> None:
        self.values = args

# Работает с любым количеством типов!
pair = Tuple[str, int]("hello", 42)
triple = Tuple[str, int, bool]("world", 100, True)
# %% [markdown]
# Кроме того, в рамках изменений типизации в 3.12 в Python также добавили новый краткий синтаксис псевдонимов типов!
# %% [python]

# СТАРЫЙ СИНТАКСИС — Python с 3.5 по 3.9
from typing import NewType
Vector = NewType("Vector", list[float])
# %% [python]

# МЕНЕЕ СТАРЫЙ СИНТАКСИС — Python с 3.10 по 3.11
from typing import TypeAlias
Vector: TypeAlias = list[float]
# %% [python]

# НОВЫЙ СИНТАКСИС — Python 3.12+
type Vector = list[float]
# %% [markdown]
# ▍ Дополнительные ресурсы
# %% [markdown]
# * Blog on Python 3.12 Generics
# * Python 3.12 Preview: Static Typing Improvements
# * Python Docs — Generics
# * PEP 695 — Type Parameter Syntax
# %% [markdown]
# 5. Протоколы
# %% [markdown]
# Одна из самых важных фич Python (и одна из основных причин для жалоб) — это его утиная типизация. Есть такая поговорка:
# %% [markdown]
# «Если это выглядит как утка, плавает как утка и крякает как утка, то это, вероятно, и есть утка».
# %% [markdown]
# Однако при этом возникает вопрос: как типизировать утиную типизацию?
# %% [python]

class Duck:
    def quack(self): print('Quack!')

class Person:
    def quack(self): print("I'm quacking!")

class Dog:
    def bark(self): print('Woof!')

def run_quack(obj):
    obj.quack()

run_quack(Duck())  # Работает!
run_quack(Person())  # Работает!
run_quack(Dog())  # Сбой с AttributeError
# %% [markdown]
# Здесь на помощь приходят протоколы. Протоколы (также называемые Structural Subtyping) — это классы типизации в Python, определяющие допустимые структуру и поведение классов без использования интерфейсов и наследования.
# %% [python]

from typing import Protocol

class Quackable(Protocol):
    def quack(self) -> None:
        ...  # Многоточие здесь означает, что это только сигнатура метода

class Duck:
    def quack(self): print('Quack!')

class Dog:
    def bark(self): print('Woof!')

def run_quack(obj: Quackable):
    obj.quack()

run_quack(Duck())  # Работает!
run_quack(Dog())  # Сбой на этапе КОНТРОЛЯ ТИПОВ (не в среде исполнения)
# %% [markdown]
# По сути, протоколы проверяют, что может делать ваш объект, а не что он делает. Они просто постулируют, что пока объект реализует определённые методы или поведения, он приемлем, вне зависимости от истинного типа или наследования.
# %% [markdown]
# Дополнительная подсказка: можно добавить декоратор @runtime_checkable, если требуется, чтобы наряду с протоколами работали проверки isinstance()!
# %% [python]

@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> None:
        ...
# %% [markdown]
# ▍ Дополнительные ресурсы
# %% [markdown]
# * Python Protocols: Leveraging Structural Subtyping
# * MyPy: Protocols and structural subtyping
# * Python Docs — Protocols
# * PEP 544 — Protocols: Structural subtyping
# %% [markdown]
# 6. Менеджеры контекста
# %% [markdown]
# Менеджеры контекста (Context Manager) — это объекты, определяющие методы: __enter__() и __exit__(). Метод __enter__() выполняется, когда мы входим в блок with, а метод __exit__() — когда мы его покидаем (даже если происходит исключение).
# %% [markdown]
# Contextlib упрощает этот процесс, оборачивая весь этот код бойлерплейта в единый удобный декоратор.
# %% [python]

# СТАРЫЙ СИНТАКСИС — Традиционный менеджер контекста в стиле ООП
class retry:
    def __enter__(self):
        print("Entering Context")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting Context")
# %% [python]

# НОВЫЙ СИНТАКСИС — Новый менеджер контекста на основе contextlib
import contextlib

@contextlib.contextmanager
def retry():
    print("Entering Context")
    yield
    print("Exiting Context")
# %% [markdown]
# Для создания своего менеджера нужно написать функцию с декоратором @contextlib.contextmanager, добавить код подготовки до yield и код подчистки после него. Все переменные в yield будут переданы дополнительному контексту. Всё просто.
# %% [markdown]
# Оператор yield приказывает менеджеру контекста поставить вашу функцию на паузу и позволяет выполниться содержимому в блоке with.
# %% [python]

import contextlib

@contextlib.contextmanager
def context():
    # Здесь код подготовки
    setup()
    yield (...)  # Все переменные, которые нужно передать блоку with
    # Здесь код очистки
    takedown()
# %% [markdown]
# В целом, это гораздо более краткий и читаемый способ создания и использования менеджеров контекста в Python.
# %% [markdown]
# ▍ Дополнительные ресурсы
# %% [markdown]
# * Context Managers and Python’s with Statement
# * Python Tips: Context Manager
# * Python Docs: contextlib — Utilities for with-statement contexts
# %% [markdown]
# 7. Структурное сопоставление с образцом
# %% [markdown]
# Появившееся в Python 3.10 структурное сопоставление с образцом (Structural Pattern Matching) предоставляет разработчикам на Python мощную альтернативу традиционной условной логике. В простейшем виде его синтаксис выглядит так:
# %% [python]

match value:
    case pattern1:
        # код, если значение соответствует pattern1
    case pattern2:
        # код, если значение соответствует pattern2
    case _:
        # подстановочный случай (по умолчанию)
# %% [markdown]
# Реальная его мощь приходит с деструктуризацией! Сопоставление шаблонов разбивает сложные структуры данных и извлекает значения за один шаг.
# %% [python]

# Деструктуризация и сопоставление кортежей
match point:
    case (0, 0):
        return "Origin"
    case (0, y):
        return f"Y-axis at {y}"
    case (x, 0):
        return f"X-axis at {x}"
    case (x, y):
        return f"Point at ({x}, {y})"
# %% [python]

# Использование шаблона OR (|) для сопоставления нескольких шаблонов
match day:
    case ("Monday"
          | "Tuesday"
          | "Wednesday"
          | "Thursday"
          | "Friday"):
        return "Weekday"
    case "Saturday" | "Sunday":
        return "Weekend"
# %% [python]

# Граничные операторы со встроенными операторами if
match temperature:
    case temp if temp < 0:
        return "Freezing"
    case temp if temp < 20:
        return "Cold"
    case temp if temp < 30:
        return "Warm"
    case _:
        return "Hot"
# %% [python]

# Сопоставляем коллекции целиком при помощи (*)
match numbers:
    case [f]:
        return f"First: {f}"
    case [f, l]:
        return f"First: {f}, Last: {l}"
    case [f, *m, l]:
        return f"First: {f}, Middle: {m}, Last: {l}"
    case []:
        return "Empty list"
# %% [markdown]
# Также можно комбинировать match-case с другими фичами Python, например, с моржовыми операторами для создания ещё более мощных шаблонов.
# %% [python]

# Проверяем валидность пакета
packet: list[int] = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07]

match packet:
    case [c1, c2, *data, footer] if (  # Деконструируем пакет на заголовок, данные и конец
        (checksum := c1 + c2) == sum(data) and  # Проверяем корректность контрольной суммы
        len(data) == footer  # Проверяем корректность размера данных
    ):
        print(f"Packet received: {data} (Checksum: {checksum})")
    case [c1, c2, *data]:  # Случай сбоя, когда структура корректна, но контрольная сумма неверна
        print(f"Packet received: {data} (Checksum Failed)")
    case [_, *__]:  # Случай сбоя, когда пакет слишком короткий
        print("Invalid packet length")
    case []:  # Случай сбоя, когда пакет пустой
        print("Empty packet")
    case _:  # Случай сбоя, когда пакет невалиден
        print("Invalid packet")
# %% [markdown]
# ▍ Дополнительные ресурсы
# %% [markdown]
# * Structural Pattern Matching in Python
# * Structural pattern matching in Python 3.10
# * Good StackOverflow Thread
# * Python Docs: The match statement
# * PEP 634 — Structural Pattern Matching: Specification
# * PEP 636 — Structural Pattern Matching: Tutorial
# %% [markdown]
# 8. Слоты Python
# %% [markdown]
# Слоты (Slots) — это способ потенциального ускорения создания любого класса Python и доступа к нему.
# %% [markdown]
# TLDR: слоты определяют фиксированное множество атрибутов для классов, оптимизируют и ускоряют операции доступа в среде исполнения.
# %% [python]

class Person:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age
# %% [markdown]
# Классы Python хранят атрибуты экземпляров во внутреннем словаре __dict__, то есть каждый раз для доступа к значению требуется поиск по хэш-таблице.
# %% [markdown]
# __slots__ использует похожую на массив структуру, где поиск атрибутов можно выполнять за время O(1), что немного ускоряет выполнение кода на Python.
# %% [python]

# Без __slots__
class FooBar:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

f = FooBar()
print(f.__dict__)  # {'a': 1, 'b': 2, 'c': 3}
# %% [python]

# Со __slots__
class FooBar:
    __slots__ = ('a', 'b', 'c')

    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

f = FooBar()
print(f.__dict__)  # AttributeError
print(f.__slots__)  # ('a', 'b', 'c')
# %% [markdown]
# По-прежнему ведутся споры о том, стоит ли пользоваться __slots__, поскольку они усложняют определения классов, не принося или почти не принося никаких улучшений производительности. Однако это полезный инструмент, который можно взять в свой арсенал и использовать по необходимости.
# %% [markdown]
# ▍ Дополнительные ресурсы
# %% [markdown]
# * Using Slots — Python Wiki
# * Don’t forget about __slots__ in Python!
# * StackOverflow — Usage of __slots__
# %% [markdown]
# 9. Мелочи Python
# %% [markdown]
# Само по себе это не «фича» Python и не «совет», а набор кратких подсказок о синтаксисе, способных повысить чистоту кодовой базы на Python.
# %% [markdown]
# 9.1 Операторы For-else
# %% [markdown]
# Если вам нужно проверить, выполняется ли цикл for без break, то это можно прекрасно сделать с помощью операторов for-else без использования временной переменной.
# %% [python]

# ===== Не пишите такой код =====
found_server = False  # Проверяем, найден ли сервер
for server in servers:
    if server.check_availability():
        primary_server = server
        found_server = True  # Присваиваем флагу значение True
        break
if not found_server:
    # Если сервер не найден, используем резервный сервер
    primary_server = backup_server

# Продолжаем исполнение с найденным сервером
deploy_application(primary_server)

# ===== Пишите так =====
for server in servers:
    if server.check_availability():
        primary_server = server
        break
else:
    # Если сервер не найден, используем резервный сервер
    primary_server = backup_server

# Продолжаем исполнение с найденным сервером
deploy_application(primary_server)
# %% [markdown]
# 9.2 Моржовый оператор
# %% [markdown]
# Если вам нужно определить и вычислить переменную в одном выражении, то для этого идеально подойдёт моржовый оператор (появившийся в Python 3.8 и PEP 572).
# %% [markdown]
# Моржовый оператор очень полезен при использовании значения сразу после проверки того, что оно not None.
# %% [python]

# ===== Не пишите такой код =====
response = get_user_input()
if response:
    print('You pressed:', response)
else:
    print('You pressed nothing')

# ===== Пишите так =====
if response := get_user_input():
    print('You pressed:', response)
else:
    print('You pressed nothing')
# %% [markdown]
# 9.3 Вычисления по короткой схеме
# %% [markdown]
# Вычисления по короткой схеме (Short-circuit Evaluation) — это быстрый способ получения «следующего доступного» или «следующего подлинного» значения в списке вычислений. Оказывается, операторы or можно просто соединять в цепочки!
# %% [python]

# ===== Не пишите такой код =====
username, full_name, first_name = get_user_info()

if username is not None:
    display_name = username
elif full_name is not None:
    display_name = full_name
elif first_name is not None:
    display_name = first_name
else:
    display_name = "Anonymous"

# ===== Пишите так =====
username, full_name, first_name = get_user_info()

display_name = username or full_name or first_name or "Anonymous"
# %% [markdown]
# 9.4 Объединение операторов в цепочки
# %% [markdown]
# Наконец, Python позволяет соединять в цепочки операторы сравнения, чтобы укоротить сравнения в интервале integer, делая их более читаемыми, чем эквивалентные булевы выражения.
# %% [python]

# ===== Не пишите такой код =====
if 0 < x and x < 10:
    print("x is between 0 and 10")

# ===== Пишите так =====
if 0 < x < 10:  # Вместо if 0 < x and x < 10
    print("x is between 0 and 10")
# %% [markdown]
# ▍ Дополнительные ресурсы
# %% [markdown]
# * for/else — Python Tips
# * The Walrus Operator: Python’s Assignment Expressions
# * PEP 572 — Assignment Expressions
# * Using the “or” Boolean Operator in Python
# * Chaining Comparison Operators
# %% [markdown]
# 10. Расширенное форматирование f-строк
# %% [markdown]
# F-строки Python уже ни для кого не являются секретом. Это более качественный, быстрый и безопасный способ интерполяции переменных, объектов и выражений в строки, появившийся в Python 3.6 и PEP 498.
# %% [markdown]
# Но знали ли вы, что f-строки позволяют не только вставлять переменные? Существует тайный синтаксис форматирования Format Mini-Language, который позволяет обеспечить гораздо больше контроля за форматированием строк.
# %% [python]

print(f"{' [ Run Status ] ':=^50}")
print(f"[{time:%H:%M:%S}] Training Run {run_id=} status: {progress:.1%}")
print(f"Summary: {total_samples:,} samples processed")
print(f"Accuracy: {accuracy:.4f} | Loss: {loss:#.3g}")
print(f"Memory: {memory / 1e9:+.2f} GB")

# Вывод:

# =================== [ Run Status ] ===================
# [11:16:37] Training Run run_id=42 status: 87.4%
# Summary: 12,345,678 samples processed
# Accuracy: 0.9876 | Loss: 0.0123
# Memory: +2.75 GB
# %% [markdown]
# С его помощью можно включать отладочные выражения, применять форматирование чисел (как при помощи str.format), добавлять заполнение строк, форматировать объекты datetime и делать многое другое! И всё это при помощи спецификаторов формата f-строк.
# %% [markdown]
# Обычные f-строки
# %% [python]

print(f"Hello {item}!")
# %% [markdown]
# Отладочные выражения
# %% [python]

print(f"{name=}, {age=}")

name='Claude', age=3
# %% [markdown]
# Форматирование чисел
# %% [python]

print(f"Pi: {pi:.2f}")
print(f"Avogadro: {avogadro:.2e}")
print(f"Big Number: {big_num:,}")
print(f"Hex: {num:#0x}")
print(f"Number: {num:09}")

# Pi: 3.14
# Avogadro: 6.02e+23
# Big Number: 1,000,000
# Hex: 0x1a4
# Number: 000000420
# %% [markdown]
# Заполнение строк
# %% [python]

print(f"Left: |{word:<10}|")
print(f"Right: |{word:>10}|")
print(f"Center: |{word:^10}|")
print(f"Center *: |{word:*^10}|")

# Left: |Python    |
# Right: |    Python|
# Center: |  Python  |
# Center *: |**Python**|
# %% [markdown]
# Форматирование дат

print(f"Date: {now:%Y-%m-%d}")
print(f"Time: {now:%H:%M:%S}")

# Date: 2025-03-10
# Time: 14:30:59
# %% [markdown]
# Форматирование процентов
# %% [python]

print(f"Progress: {progress:.1%}")

# Progress: 75.0%
# %% [markdown]
# ▍ Дополнительные ресурсы
# %% [markdown]
# * Python’s F-String for String Interpolation and Formatting
# * Python’s Format Mini-Language for Tidy Strings
# * Python Docs — Input and Output
# * PEP 498 — Literal String Interpolation
# %% [markdown]
# 11. cache/lru_cache
# %% [markdown]
# Можно использовать встроенный декоратор @cache, чтобы существенно ускорить рекурсивные функции и затратные вычисления! (В Python 3.9 он вытеснил @lru_cache.)
# %% [python]

from functools import cache

@cache
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)
# %% [markdown]
# В Python 3.2 @lru_cache появился как часть модуля functools и был предназначен для быстрой и чистой мемоизации функций. В Python 3.9 был добавлен @cache, позволяющий добиться того же результата с меньшим количеством кода. Если вам нужен непосредственный контроль над размером кэша, то можно по-прежнему использовать lru_cache.
# %% [python]

FIB_CACHE = {}

# С ручным кэшированием
def fib(n):
    if n in FIB_CACHE:
        return FIB_CACHE[n]
    if n <= 2:
        return 1
    FIB_CACHE[n] = fib(n - 1) + fib(n - 2)
    return FIB_CACHE[n]

from functools import lru_cache

# Тот же код с lru_cache
@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

from functools import cache

# Тот же код с новым кэшем Python 3.9
@cache
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)
# %% [markdown]
# ▍ Дополнительные ресурсы
# %% [markdown]
# * Python Cache: Two Simple Methods
# * (outdated) Caching in Python Using the LRU Cache Strategy
# * Python Docs — @functools.cache
# * Python Docs — @functools.lru_cache
# %% [markdown]
# 12. Python Futures
# %% [markdown]
# А вы знали, что в Python есть нативное управление конкурентностью в стиле Promise?
# %% [python]

from concurrent.futures import Future

# Создаём вручную объект Future
future = Future()

# Задаём ему любой нужный результат
future.set_result("Hello from the future!")

# Получаем результат
print(future.result())  # "Hello from the future!"
# %% [markdown]
# Модуль concurrent.futures языка Python даёт нам непосредственный контроль над async-операциями, как Promise в JS. Например, он позволяет прикреплять обратные вызовы, запускаемые при готовности результата (точно так же, как .then() в JS).
# %% [python]

from concurrent.futures import Future

future = Future()

# Добавляем обратные вызовы ДО или ПОСЛЕ завершения!
future.add_done_callback(lambda f: print(f"Got: {f.result()}"))

future.set_result("Async result")
# Вывод: "Got: Async result"

future.add_done_callback(lambda f: print(f"After: {f.result()}"))
# Вывод: "After: Async result"
# %% [markdown]
# Также у Python Futures есть примитивы для обработки исключений, задания таймаутов и полной остановки задач.
# %% [python]

from concurrent.futures import Future
import time, threading

# Создаём future и управляем им вручную
future = Future()

# Функция фоновой задачи
def background_task():
    time.sleep(2)
    future.set_result("Done!")

thread = threading.Thread(target=background_task)
thread.daemon = True
thread.start()

# Пробуем все операции управления
print(f"Cancelled: {future.cancel()}")  # Скорее всего, False, если запустилось

try:
    # Ждём не больше 0,5 секунды
    result = future.result(timeout=0.5)
except TimeoutError:
    print("Timed out!")

# Создаём future сбоя
err_future = Future()
err_future.set_exception(ValueError("Failed"))
print(f"Has error: {bool(err_future.exception())}")
# %% [markdown]
# Как и в современном JS, модуль asyncio имеет собственный Future, идеально работающий с синтаксисом async/await Python:
# %% [python]

import asyncio

async def main():
    future = asyncio.Future()

    # Задаём результат после задержки
    asyncio.create_task(set_after_delay(future))

    # Await, как Promise в JS!
    result = await future
    print(result)  # "Worth the wait!"

async def set_after_delay(future):
    await asyncio.sleep(1)
    future.set_result("Worth the wait!")

asyncio.run(main())
# %% [markdown]
# Наконец, для задач, сильно зависящих от ресурсов CPU или ввода-вывода, ThreadPoolExecutor может автоматически создавать future и управлять ими.
# %% [python]

from concurrent.futures import ThreadPoolExecutor
import time

def slow_task():
    time.sleep(1)
    return "Done!"

with ThreadPoolExecutor() as executor:
    # Немедленно возвращает Future
    future = executor.submit(slow_task)

    # Пока ожидаем, выполняем другую работу...
    print("Working...")

    # Получаем результат по необходимости
    print(future.result())
# %% [markdown]
# ▍ Дополнительные ресурсы
# %% [markdown]
# * Introduction to concurrent.futures in Python
# * Adventures in Python with concurrent.futures
# * Python Docs — Futures
# * Python Docs — concurrent.futures
# %% [markdown]
# 13. Прокси-свойства
# %% [markdown]
# А вы знали, что атрибуты классов могут использоваться одновременно как методы И свойства? Это не встроенная фича Python, а демонстрация того, что можно сделать благодаря хитрому использованию dunder-методов и дескрипторов Python.
# %% [markdown]
# (Учтите, что это пример реализации, который нельзя использовать в продакшене)
# %% [python]

from typing import Callable, Generic, TypeVar, ParamSpec, Self

P = ParamSpec("P")
R = TypeVar("R")
T = TypeVar("T")

class ProxyProperty(Generic[P, R]):
    func: Callable[P, R]
    instance: object

    def __init__(self, func: Callable[P, R]) -> None:
        self.func = func

    def __get__(self, instance: object, _=None) -> Self:
        self.instance = instance
        return self

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R:
        return self.func(self.instance, *args, **kwargs)

    def __repr__(self) -> str:
        return self.func(self.instance)

def proxy_property(func: Callable[P, R]) -> ProxyProperty[P, R]:
    return ProxyProperty(func)

class Container:
    @proxy_property
    def value(self, val: int = 5) -> str:
        return f"The value is: {val}"

# Пример использования 
c = Container()
print(c.value)      # Возвращает: The value is: 5
print(c.value(7))   # Возвращает: The value is: 7
# %% [markdown]
# Всё сводится к Descriptor Protocol Python:
# %% [markdown]
# * Метод __get__ преобразует объект ProxyProperty в дескриптор.
# * При выполнении доступа к c.value Python вызывает __get__, который возвращает self (экземпляр дескриптора).
# * Метод __repr__ обрабатывает доступ к свойствам (возвращая значения по умолчанию).
# * Метод __call__ обрабатывает вызовы методов с параметрами.
# %% [markdown]
# Это создаёт атрибут двойного назначения, который и можно считывать напрямую, И вызывать как функцию!
# %% [markdown]
# Преимущество этого класса в том, что он позволяет нам создавать интуитивно понятные API, в которых свойству может требоваться конфигурация, или если им нужны свойства, которые должны иметь разумные значения по умолчанию, но в то же время доступны для изменения.
# %% [markdown]
# Если вы хотите посмотреть на готовую к продакшену реализацию прокси-свойств, то изучите реализацию ProxyProperty Codegen: codegen/src/codegen/sdk/_proxy.py
# %% [markdown]
# ▍ >Дополнительные ресурсы
# %% [markdown]
# * Python Descriptors: An Introduction
# * Demystifying Python’s Descriptor Protocol
# * Descriptor Guide — Python Wiki
# * Proxies and Wrappers
# %% [markdown]
# 14. Метаклассы
# %% [markdown]
# В конце я хочу рассказать об одной из самых мощных, но загадочных фич: о метаклассах.
# %% [python]

class MyMetaclass(type):
    def __new__(cls, name, bases, namespace):
        # Магия происходит здесь
        return super().__new__(cls, name, bases, namespace)

class MyClass(metaclass=MyMetaclass):
    pass

obj = MyClass()
# %% [markdown]
# Классы в Python — это не просто «схемы» для объектов. Они тоже являются объектами! А каждому объекту требуется создающий его класс. Так что же создаёт объекты-классы? Метаклассы.
# %% [markdown]
# По умолчанию, Python использует для создания всех классов метакласс type. Например, эти два примера кода эквивалентны друг другу:
# %% [python]

# Создаём объект MyClass
class MyClass:
    ...
obj = MyClass()

# Тоже создаём объект MyClass
obj2 = type("MyClass", (), {})
# %% [markdown]
# Чтобы разобраться, что означают эти аргументы, приведём пример, создающий класс с атрибутом x и методом say_hi, которые также являются подклассами object.
# %% [python]

# type(
#     name,
#     bases,
#     attributes
# )
CustomClass = type(
    'CustomClass',
    (object,),
    {'x': 5, 'say_hi': lambda self: 'Hello!'}
)

obj = CustomClass()
print(obj.x)  # 5
print(obj.say_hi())  # Hello!
# %% [markdown]
# По сути, метаклассы позволяют настраивать и изменять эти аргументы в процессе создания классов. Например, вот метакласс, удваивающий каждый атрибут integer для класса:
# %% [python]

class DoubleAttrMeta(type):
    def __new__(cls, name, bases, namespace):
        new_namespace = {}
        for key, val in namespace.items():
            if isinstance(val, int):
                val *= 2
            new_namespace[key] = val
        return super().__new__(cls, name, bases, new_namespace)

class MyClass(metaclass=DoubleAttrMeta):
    x = 5
    y = 10

print(MyClass.x)  # 10
print(MyClass.y)  # 20
# %% [markdown]
# Вот ещё один пример метакласса, заносящий каждый созданный класс в registry.
# %% [python]

# ===== Решение с метаклассом =====
class RegisterMeta(type):
    registry = []
    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)
        mcs.registry.append(cls)
        return cls
# %% [markdown]
# Проблема в том, что декораторы могут решать ту же самую задачу без использования чёрной магии (и код часто оказывается при этом чище).
# %% [python]

# ===== Решение с декоратором =====
def register(cls):
    registry.append(cls)
    return cls

@register
class MyClass:
    pass
# %% [markdown]
# И это подчёркивает самую большую проблему метаклассов:
# %% [markdown]
# Почти в 100% случаев вам они не понадобятся.
# %% [markdown]
# В повседневной разработке 99% кода не будет даже затрагивать те сценарии использования, в которых были бы полезны метаклассы. А из оставшегося 1% в 95% случаев задачу можно решать при помощи обычных декораторов, dunder-методов и просто наследования.
# %% [markdown]
# Именно поэтому возникло знаменитое изречение о Python:
# %% [markdown]
# «Метаклассы — это такая глубокая магия, что 99% пользователей не стоит о ней думать. Если вы задаётесь вопросом, нужны ли они вам, то они вам не нужны». — Тим Питерс
# %% [markdown]
# Но если вы входите в тот 1%, у которого есть уникальная задача, решаемая только при помощи метаклассов, то они окажутся мощным инструментом, позволяющим работать с внутренним устройством системы объектов Python.
# %% [markdown]
# Несколько примеров реального использования метаклассов:
# %% [markdown]
# Реализация «ABC» Python использует метаклассы для реализации абстрактных классов.
# В реализации «Enum» Python они используются для создания типов перечислений.
# Некоторые сторонние библиотеки, например, Django, SQLAlchemy, Pydantic и Pytest, используют для различных целей метаклассы.
# %% [markdown]
# ▍ Дополнительные ресурсы
# %% [markdown]
# * Python Metaclasses
# * What are Python Metaclasses?
# * Demystifying Python Metaclasses
# * Re: The metaclass saga using Python
# %% [markdown]
# Завершение
# %% [markdown]
# Вот, собственно, и всё! Я рассказал о 14 самых интересных и недооценённых фич Python, встречавшихся мне в моей карьере разработчика на Python.
# %%
