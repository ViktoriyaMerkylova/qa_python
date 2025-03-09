import pytest
from conftest import non_book
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    #1.Положительный сценарий: добавляеи одну книгу
    def test_add_new_book_add_one_book(self, collector):
        collector.add_new_book(non_book)
        assert len(collector.get_books_genre()) == 1

    # 2.Проверка ограничений по длине: название длиннее 40 символов
    def test_add_new_book_title_longer_than_40_chars(self, collector):
        collector.add_new_book("а" * 41)
        assert "а" * 41 not in collector.books_genre

    # 3.Позитивный сценарий: книга есть в словаре, жанр входит в список, жанр менятся
