# https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-19-osnovy-oop-abstrakciya-i-polimorfizm-2023-04-24

from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def get_summary(self):
        pass

class Fiction(Book):
    def get_summary(self):
        print(f'"{self.title}" - роман в стиле исторический фикшн, автор - {self.author}')

class NonFiction(Book):
    def get_summary(self):
        print(f'"{self.title}" - книга в стиле нон фикшн, автор - {self.author}')

class Poetry(Book):
    pass

fiction_book = Fiction("Террор", "Дэн Симмонс")
nonfiction_book = NonFiction("Как писать книги", "Стивен Кинг")
fiction_book.get_summary()
nonfiction_book.get_summary()
poetry_book = Poetry("Стихотворения", "Борис Пастернак")
