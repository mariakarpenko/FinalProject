from selenium.webdriver.common.by import By
import allure

class MainPage:
    def __init__(self, browser: str):
        """
        Функция-конструктор, создает экзмпляр класса
        """
        self._driver = browser
        self._driver.get('https://bookmate.ru/')
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Перейти на страницу поиска")
    def to_search_page(self):
        """
        Функция нажимает на иконку поиска (лупа) для перехода на страницу поиска
        """
        self._driver.find_element(By.CSS_SELECTOR, 'a[data-e2e="navigation.search"]').click()



class SearchPage:
    def __init__(self, browser: str):
        """
        Функция-конструктор, создает экзмпляр класса
        """
        self._driver = browser
        self._driver.get('https://bookmate.ru/search')
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Ввести текст в поисковую строку")
    def search(self, input: str):
        """
        Функция вводит текст в поисковую строку \n
        (по мере печати на странице отображаются результаты поиска)
        """
        self._driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Книги, авторы, жанры"]').send_keys(input)



class TextBookPage:
    def __init__(self, browser: str, book_id:str):
        """
        Функция-конструктор, создает экзмпляр класса
        """
        self._driver = browser
        self._driver.get('https://bookmate.ru/books/' + book_id)
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Нажать на кнопку 'Читать' на странице текстовой книги")
    def press_read_button(self):
        """
        Функция нажиает на кнопку "Читать" на странице книги
        """
        self._driver.find_element(By.XPATH, "//*[text()='Читать']").click()



class ComicBookPage:
    def __init__(self, browser: str, comicbook_id:str):
        """
        Функция-конструктор, создает экзмпляр класса
        """
        self._driver = browser
        self._driver.get('https://bookmate.ru/comicbooks/' + comicbook_id)
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Нажать на кнопку 'Читать в приложении' на странице комикса")
    def press_read_on_app_button(self):
        """
        Функция нажиает на кнопку "Читать в приложении" на странице комикса
        """
        self._driver.find_element(By.XPATH, "//*[text()='Читать в приложении']").click()