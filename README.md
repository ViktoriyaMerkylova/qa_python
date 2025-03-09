#Sprint#4

### Методы класса BooksCollector и их тестовое покрытие

| Метод        |                                                                       Описание метода                                                                        |                                                                                                                                                                                                                      Проверка метода |
| ------------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------:|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| ```add_new_book```    | 1.Добавление одной книги.<br/> 2.Проверка ограничений по длине: название длинее 40 символов.|```test_add_new_book_add_one_book``` <br/> ```test_add_new_book_title_longer_than_40_chars```|
| ```set_book_genre```  | 3.Присвоение книги жанра <br/> 4.Добавление жанра, который не входит в список. |```test_set_book_genre_valid_inputs``` <br/>  ```test_set_book_genre_not_in_list```|
| ```get_book_genre```| 5.Поиск жанра по ее книге.|```test_get_book_genre_existing_book```|
| ```get_books_with_specific_genre```| 6.Книга существует, но жанр не установлен. |```test_get_books_with_specific_genre_existing_book```  |
| ```get_books_for_children```|7.Проверка исключения книг с возратсным рейтингом.|```test_get_books_for_children_valid_books``` |
| ```add_book_in_favorites```|8.Добавление в избранное. | ```test_add_book_in_favorites_success``` |
| ```delete_book_from_favorites```| 9.Удаление книги из избранного.| ```test_delete_book_positive_scenario``` |
| ```get_list_of_favorites_books```| 10. Получение пустого списка избранных| ```test_get_empty_favorites_books_list``` |


