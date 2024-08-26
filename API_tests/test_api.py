import json
import pytest
import requests
import psycopg2
import allure

from API_tests.long_variables import *
from API_tests.APISearchPage import SearchPage

search_page = SearchPage('https://bookmate.ru/node-api/p-graphql/')

@allure.id("1")
@allure.epic("API-тестирование")
@allure.feature("Поиск")
@allure.suite("Позитивные проверки")
@allure.title("Поиск без опечаток")
@allure.description("Поиск с вводом валидного запроса без содержания опечаток")
@allure.severity("Critical")
def test_search_without_misprints():
    with allure.step("Отправить POST-запрос на поиск книги"):
        sought_for_book = "Анна Каренина"
        search_response = search_page.search_among_all(sought_for_book)

    with allure.step("Убедиться, что статус-код ответа - 200"):
        assert search_response.status_code == 200

    with allure.step("Убедиться, что в теле ответа содержится искомый текст"):
        assert sought_for_book in search_response.json()["data"]["search"]["page"][0]["book"]["name"]

@allure.id("2")
@allure.epic("API-тестирование")
@allure.feature("Поиск")
@allure.suite("Позитивные проверки")
@allure.title("Поиск с опечатками")
@allure.description("Поиск с вводом валидного запроса при наличии опечаток")
@allure.severity("Critical")
def test_search_with_misprints():
    with allure.step("Отправить POST-запрос на поиск книги"):
        sought_for_book = "Преступление и наказание"
        factual_input = "Приступление и ноказание"
        search_response = search_page.search_among_all(factual_input)

    with allure.step("Убедиться, что статус-код ответа - 200"):
        assert search_response.status_code == 200

    with allure.step("Убедиться, что в теле ответа содержится искомый текст"):
        assert sought_for_book in search_response.json()["data"]["search"]["misspell"]["correctedText"]



@allure.id("3")
@allure.epic("API-тестирование")
@allure.feature("Поиск")
@allure.suite("Позитивные проверки")
@allure.title("Поиск автора на латинице")
@allure.description("Поиск автора с вводом валидного запроса составленного из символов латиницы")
@allure.severity("Critical")
def test_search_author_latin():
    with allure.step("Отправить POST-запрос на поиск книги"):
        sought_for_author_latin = "Charlotte Brontë"
        sought_for_author_cyrillic = "Шарлотта Бронте"
        search_response = search_page.search_among_all(sought_for_author_latin)

    with allure.step("Убедиться, что статус-код ответа - 200"):
        assert search_response.status_code == 200

    with allure.step("Убедиться, что в теле ответа содержится искомый текст"):
        assert sought_for_author_cyrillic in search_response.json()["data"]["search"]["page"][0]["name"]



@allure.id("4")
@allure.epic("API-тестирование")
@allure.feature("Поиск")
@allure.suite("Позитивные проверки")
@allure.title("Поиск книги на латинице")
@allure.description("Поиск книги с вводом валидного запроса составленного из символов латиницы")
@allure.severity("Critical")
def test_search_book_latin():
    with allure.step("Отправить POST-запрос на поиск книги"):
        sought_for_book_latin = "Dracula"
        sought_for_book_cyrillic = "Дракула"
        search_response = search_page.search_among_all(sought_for_book_latin)

    with allure.step("Убедиться, что статус-код ответа - 200"):
        assert search_response.status_code == 200

    with allure.step("Убедиться, что в теле ответа содержится искомый текст"):
        assert sought_for_book_cyrillic in search_response.json()["data"]["search"]["page"][0]["book"]["name"]



@allure.id("5")
@allure.epic("API-тестирование")
@allure.feature("Поиск")
@allure.suite("Негативные проверки")
@allure.title("Поиск по названию книги в разделе 'Авторы'")
@allure.description("Поиск книги по ее названию в разделе 'Авторы'")
@allure.severity("Critical")
def test_search_book_in_authors():
    with allure.step("Отправить POST-запрос на поиск книги в разделе 'Авторы'"):
        sought_for_book = "Женщина французского лейтенанта"
        section_name = 'AUTHOR'
        search_response = search_page.search_in_section(sought_for_book, section_name)

    with allure.step("Убедиться, что статус-код ответа - 200"):
        assert search_response.status_code == 200

    with allure.step("Убедиться, что количество найденных единиц равно нулю"):
        items_found = search_response.json()["data"]["search"]["page"]
        assert len(items_found) == 0



@allure.id("6")
@allure.epic("API-тестирование")
@allure.feature("Поиск")
@allure.suite("Негативные проверки")
@allure.title("Пустая поисковая строка")
@allure.description("Поиск при пустой поисковой строке")
@allure.severity("Critical")
def test_empty_search_field():
    with allure.step("Отправить POST-запрос на поиск с пустой поисковой строкой"):
        search_field_input = ""
        search_response = search_page.search_among_all(search_field_input)

    with allure.step("Убедиться, что статус-код ответа - 200"):
        assert search_response.status_code == 200

    with allure.step("Убедиться, что количество найденных единиц равно нулю"):
        items_found = search_response.json()["data"]["search"]["page"]
        assert len(items_found) == 0



@allure.id("7")
@allure.epic("API-тестирование")
@allure.feature("Поиск")
@allure.suite("Негативные проверки")
@allure.title("Только пробелы")
@allure.description("Поиск при вводе в поисковой строке только пробелов")
@allure.severity("Critical")
def test_only_spaces():
    with allure.step("Отправить POST-запрос на поиск только пробелов"):
        search_field_input = "         "
        search_response = search_page.search_among_all(search_field_input)

    with allure.step("Убедиться, что статус-код ответа - 200"):
        assert search_response.status_code == 200

    with allure.step("Убедиться, что количество найденных единиц равно нулю"):
        items_found = search_response.json()["data"]["search"]["page"]
        assert len(items_found) == 0



@allure.id("8")
@allure.epic("API-тестирование")
@allure.feature("Поиск")
@allure.suite("Негативные проверки")
@allure.title("Бессмысленный набор символов")
@allure.description("Поиск при вводе в поисковой строке бессмысленного набора символов")
@allure.severity("Critical")
def test_nonsesical_input():
    with allure.step("Отправить POST-запрос на поиск только пробелов"):
        search_field_input = "рлаилмиhjdbkrghuj56789jfhv"
        search_response = search_page.search_among_all(search_field_input)

    with allure.step("Убедиться, что статус-код ответа - 200"):
        assert search_response.status_code == 200

    with allure.step("Убедиться, что количество найденных единиц равно нулю"):
        items_found = search_response.json()["data"]["search"]["page"]
        assert len(items_found) == 0



@allure.id("9")
@allure.epic("API-тестирование")
@allure.feature("Поиск")
@allure.suite("Негативные проверки")
@allure.title("Более 500 символов")
@allure.description("Поиск при вводе в поисковой строке более 500 символов")
@allure.severity("Critical")
def test_over_500_symbols():
    with allure.step("Отправить POST-запрос на поиск только пробелов"):
        search_field_input = string_501_symbols
        search_response = search_page.search_among_all(search_field_input)

    with allure.step("Убедиться, что статус-код ответа - 200"):
        assert search_response.status_code == 200

    with allure.step("Убедиться, что количество найденных единиц равно нулю"):
        items_found = search_response.json()["data"]["search"]["page"]
        assert len(items_found) == 0