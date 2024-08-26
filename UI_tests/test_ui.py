from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import allure

from UI_tests.WebPages import MainPage, SearchPage, TextBookPage, ComicBookPage

@allure.id("1")
@allure.epic("UI-тестирование")
@allure.feature("Поиск")
@allure.title("Пробелы до текста")
@allure.description("Поиск книги при добавлении прбелов в запросе перед самим текстом с названием книги")
@allure.severity("Major")
def test_search_spaces_before_text():
    browser = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

    with allure.step("Предусловия"):
        with allure.step("Перейти на страницу Bookmate в браузере Google Chrome"):
            main_page = MainPage(browser)

    with allure.step("Нажать на иконку поиска (лупа) для перехода на страницу поиска"):
        main_page.to_search_page()
        search_page = SearchPage(browser)

    with allure.step("Ввести текст в поисковую строку"):
        book_title_with_spaces = '       Мельмот Скиталец'
        search_page.search(book_title_with_spaces)

    with allure.step("Убедиться, что на странице название одной из книг соответствует поисковому запросу без пробелов в начале"):
        book_title_no_spaces = 'Мельмот Скиталец'
        one_of_books_title = browser.find_element(By.CSS_SELECTOR, 'a[href="/books/eIrrtHjr"]').text
        assert one_of_books_title == book_title_no_spaces

    with allure.step("Закрыть браузер"):
        browser.quit()



@allure.id("2")
@allure.epic("UI-тестирование")
@allure.feature("Поиск")
@allure.title("Иероглифы")
@allure.description("Ввод иероглифов при поиске")
@allure.severity("Major")
def test_search_hieroglyphs():
    browser = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

    with allure.step("Предусловия"):
        with allure.step("Перейти на страницу Bookmate в браузере Google Chrome"):
            main_page = MainPage(browser)

    with allure.step("Нажать на иконку поиска (лупа) для перехода на страницу поиска"):
        main_page.to_search_page()
        search_page = SearchPage(browser)

    with allure.step("Ввести иероглифический текст в поисковую строку"):
        # 'Мосян Тунсю' (Китайская писательница)
        hieroglyphic_inscription = '墨香铜臭' 
        search_page.search(hieroglyphic_inscription)

    with allure.step("Убедиться, что на странице есть результаты, соответствующие поисковому запросу"):
        element_found_on_page = browser.find_element(By.XPATH, "//*[text()='墨香铜臭']").text
        assert hieroglyphic_inscription == element_found_on_page

    with allure.step("Закрыть браузер"):
        browser.quit()



@allure.id("3")
@allure.epic("UI-тестирование")
@allure.feature("Поиск")
@allure.title("Поиск чтеца в разделе 'Рассказчики'")
@allure.description("Поиск по имени и фамилии чтеца в разделе 'Рассказчики")
@allure.severity("Major")
def test_search_reader_in_readers_section():
    browser = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

    with allure.step("Предусловия"):
        with allure.step("Перейти на страницу Bookmate в браузере Google Chrome"):
            main_page = MainPage(browser)

    with allure.step("Нажать на иконку поиска (лупа) для перехода на страницу поиска"):
        main_page.to_search_page()
        search_page = SearchPage(browser)

    with allure.step("Ввести текст в поисковую строку"):
        reader = 'Сергей Чонишвили' 
        search_page.search(reader)

    with allure.step("Выбрать раздел 'Рассказчики' среди разделов под поисковой строкой"):
        readers_section_button = "//*[text()='Рассказчики']"
        browser.find_element(By.XPATH, readers_section_button).click()

    with allure.step("Убедиться, что на странице есть чтец, соответствующий поисковому запросу"):
        reader_found_on_page = browser.find_element(By.XPATH, "//*[text()='Сергей Чонишвили']").text
        assert reader == reader_found_on_page

    with allure.step("Закрыть браузер"):
        browser.quit()



@allure.id("4")
@allure.epic("UI-тестирование")
@allure.feature("Поиск")
@allure.title("Текст только в верхнем регистре")
@allure.description("Поиск книги по ее названию, написанному только в верхнем регистре")
@allure.severity("Major")
def test_search_all_caps():
    browser = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

    with allure.step("Предусловия"):
        with allure.step("Перейти на страницу Bookmate в браузере Google Chrome"):
            main_page = MainPage(browser)

    with allure.step("Нажать на иконку поиска (лупа) для перехода на страницу поиска"):
        main_page.to_search_page()
        search_page = SearchPage(browser)

    with allure.step("Ввести текст в поисковую строку"):
        book_title_all_caps = 'ЧАЙКА'
        search_page.search(book_title_all_caps)

    with allure.step("Убедиться, что на странице название одной из книг соответствует поисковому запросу, написанному корректно"):
        book_title_original = 'Чайка'
        one_of_books_title = browser.find_element(By.CSS_SELECTOR, 'a[href="/books/DIYA2rn8"]').text
        assert one_of_books_title == book_title_original

    with allure.step("Закрыть браузер"):
        browser.quit()



@allure.id("5")
@allure.epic("UI-тестирование")
@allure.feature("Поиск")
@allure.title("Текст на неправильной раскладке")
@allure.description("Поиск книги по ее названию, написанному на неправильной раскладке")
@allure.severity("Major")
def test_search_wrong_layout():
    browser = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

    with allure.step("Предусловия"):
        with allure.step("Перейти на страницу Bookmate в браузере Google Chrome"):
            main_page = MainPage(browser)

    with allure.step("Нажать на иконку поиска (лупа) для перехода на страницу поиска"):
        main_page.to_search_page()
        search_page = SearchPage(browser)

    with allure.step("Ввести текст в поисковую строку"):
        book_title_wrong_layout = 'Ljdjls hfccelrf'
        search_page.search(book_title_wrong_layout)

    with allure.step("Убедиться, что на странице название одной из книг соответствует поисковому запросу, написанному на правильной раскладке"):
        book_title_original = 'Доводы рассудка'
        one_of_books_title = browser.find_element(By.CSS_SELECTOR, 'a[href="/books/ayc8PQ3L"]').text
        assert one_of_books_title == book_title_original

    with allure.step("Закрыть браузер"):
        browser.quit()


@allure.id("6")
@allure.epic("UI-тестирование")
@allure.feature("Открытие страницы с текстом книги / включение записи с аудиокнигой")
@allure.title("Открытие ридера к книге с текстовым форматом")
@allure.description("")
@allure.severity("Critical")
def test_open_textbook():
    browser = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

    with allure.step("Предусловия"):
        with allure.step("Перейти на страницу Bookmate в браузере Google Chrome"):
            main_page = MainPage(browser)

        with allure.step("Нажать на иконку поиска (лупа) для перехода на страницу поиска"):
            main_page.to_search_page()
            search_page = SearchPage(browser)

        with allure.step("Ввести текст в поисковую строку"):
            book_title = 'Бесы' 
            search_page.search(book_title)
        
    with allure.step("Открыть страницу книги"):
        book_button = 'a[href="/books/CWUzigfr"]'
        browser.find_element(By.CSS_SELECTOR, book_button).click()
        text_book_page = TextBookPage(browser, 'CWUzigfr')

    with allure.step("Нажать на кнопку 'Читать'"):
        text_book_page.press_read_button()

    with allure.step("Нажать на кнопку 'Назад' со страницы авторизации"):
        browser.implicitly_wait(4)
        browser.find_element(By.CSS_SELECTOR, 'a[aria-label="Назад"]').click()
        browser.implicitly_wait(4)

    with allure.step("Убедиться, что открылась страница ридера выбранной книги"):
        chosen_book_reader_url = 'https://bookmate.ru/reader/CWUzigfr?resource=book'
        current_url = browser.current_url
        assert current_url == chosen_book_reader_url

    with allure.step("Закрыть браузер"):
        browser.quit()    



@allure.id("7")
@allure.epic("UI-тестирование")
@allure.feature("Открытие страницы с текстом книги / включение записи с аудиокнигой")
@allure.title("Открытие страницы с ссылками, QR кодом на мобильное приложение, при выборе книги-комикса")
@allure.description("")
@allure.severity("Critical")
def test_open_comicbook():
    browser = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

    with allure.step("Предусловия"):
        with allure.step("Перейти на страницу Bookmate в браузере Google Chrome"):
            main_page = MainPage(browser)

        with allure.step("Нажать на иконку поиска (лупа) для перехода на страницу поиска"):
            main_page.to_search_page()
            search_page = SearchPage(browser)

        with allure.step("Ввести название комикса в поисковую строку"):
            comics_title = 'Sapiens. Графическая история. Часть 1. Рождение человечества' 
            search_page.search(comics_title)

        with allure.step("Выбрать раздел 'Комиксы' среди разделов под поисковой строкой"):
            comics_section_button = "//*[text()='Комиксы']"
            browser.find_element(By.XPATH, comics_section_button).click()
        
    with allure.step("Открыть страницу комикса"):
        book_button = 'a[href="/comicbooks/O6JHMHfC"]'
        browser.find_element(By.CSS_SELECTOR, book_button).click()
        comic_book_page = ComicBookPage(browser, 'O6JHMHfC')

    with allure.step("Нажать на кнопку 'Читать в приложении'"):
        comic_book_page.press_read_on_app_button()

    with allure.step("Убедиться, что на странице присутствует блок с QR-кодом и ссылками на приложения в разных магазинах"):
        assert browser.find_element(By.CSS_SELECTOR, 'div.store-info').is_displayed() == True

    with allure.step("Закрыть браузер"):
        browser.quit() 