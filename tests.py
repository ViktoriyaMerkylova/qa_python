import pytest
from conftest import horror_book, horror_ganre, drama_ganre
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    #1.Положительный сценарий: добавляеи одну книгу
    def test_add_new_book_add_one_book(self, collector):
        collector.add_new_book(horror_book)
        assert len(collector.get_books_genre()) == 1

    # 2.Проверка ограничений по длине: название длиннее 40 символов
    def test_add_new_book_title_longer_than_40_chars(self, collector):
        collector.add_new_book("а" * 41)
        assert "а" * 41 not in collector.books_genre

    # 3.Позитивный сценарий: проверка установления книги жанра
    def test_set_book_genre_valid_inputs(self, collector):
        collector.add_new_book(horror_book)
        collector.set_book_genre(horror_book, horror_ganre)
        assert collector.books_genre[horror_book] == horror_ganre

    #4.Негативный сценарий: жанр не входит в список
    def test_set_book_genre_not_in_list(self, collector):
        collector.add_new_book(horror_book)
        collector.set_book_genre(horror_book, drama_ganre)
        assert collector.books_genre.get(horror_book) != drama_ganre

    #5.Позитивный сценарий: поиск книги по жанру
    def test_get_book_genre_existing_book(self, collector):
        collector.add_new_book(horror_book)
        collector.set_book_genre(horror_book, horror_ganre)
        assert collector.get_books_with_specific_genre(horror_ganre) == [horror_book]