from conftest import non_book
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    #положительный сценарий: добавляеи одну книгу
    def test_add_new_book_add_one_book(self, collector):
        collector.add_new_book(non_book)
        assert len(collector.get_books_genre()) == 1
