import pytest

from main import BooksCollector

@pytest.fixture(scope="function")
def collector():
    collector = BooksCollector()
    return collector

horror_book = 'Сияние'
horror_ganre = 'Ужасы'
drama_ganre = 'Драма'