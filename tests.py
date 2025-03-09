import pytest
from conftest import horror_book, horror_ganre, drama_ganre


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    #1.Добавление одной книги.
    def test_add_new_book_add_one_book(self, collector):
        collector.add_new_book(horror_book)
        assert len(collector.get_books_genre()) == 1

    # 2.Проверка ограничений по длине: название длинее 40 символов.
    def test_add_new_book_title_longer_than_40_chars(self, collector):
        collector.add_new_book("а" * 41)
        assert "а" * 41 not in collector.books_genre

    # 3.Присвоение книги жанра
    def test_set_book_genre_valid_inputs(self, collector):
        collector.add_new_book(horror_book)
        collector.set_book_genre(horror_book, horror_ganre)
        assert collector.books_genre[horror_book] == horror_ganre

    #4.Добавление жанра, который не входит в список
    def test_set_book_genre_not_in_list(self, collector):
        collector.add_new_book(horror_book)
        collector.set_book_genre(horror_book, drama_ganre)
        assert collector.books_genre.get(horror_book) != drama_ganre

    #5.Поиск жанра по ее книге.
    def test_get_book_genre_existing_book(self, collector):
        collector.add_new_book(horror_book)
        collector.set_book_genre(horror_book, horror_ganre)
        assert collector.get_books_with_specific_genre(horror_ganre) == [horror_book]

    # 6.Книга существует, но жанр не установлен.
    def test_get_books_with_specific_genre_existing_book(self, collector):
        collector.add_new_book(horror_book)
        assert collector.get_book_genre(horror_book) == ''

    # 7.Проверка исключения книг с возратсным рейтингом.
    @pytest.mark.parametrize (
        "book_name,book_genre,expected_result",
        [
    ("Приключения пушистого облака", "Мультфильмы", True),
    ("Невинный шёпот мёртвых", "Детективы", False),
    ("Дракоша в городском Парке", "Фантастика", True),
    ("Тёмная комната свидетеля", "Ужасы", False)
        ]
    )
    def test_get_books_for_children_valid_books(self, collector, book_name,book_genre, expected_result):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        books_for_children = collector.get_books_for_children()
        if expected_result:
            assert book_name in books_for_children
        else:
            assert book_name not in books_for_children

    # 8.Добавление в избранное.
    def test_add_book_in_favorites_success(self, collector):
        collector.add_new_book(horror_book)
        collector.add_book_in_favorites(horror_book)
        assert horror_book in collector.get_list_of_favorites_books()

    # 9.Удаление книги из избранного.
    def test_delete_book_positive_scenario(self, collector):
        collector.add_new_book(horror_book)
        collector.add_book_in_favorites(horror_book)
        collector.delete_book_from_favorites(horror_book)
        assert collector.get_list_of_favorites_books() == []

    #10. Получение пустого списка избранных
    def test_get_list_of_favorites_book_list(self, collector):
        assert collector.get_list_of_favorites_books() == []


