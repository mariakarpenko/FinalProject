import requests
import json
import allure

from API_tests.long_variables import *

class SearchPage:
    def __init__(self, url: str) -> None:
        """
        Функция-конструктор, создает экземпляр класса, в параметре url указывается URL, на который будут отправляться запросы
        """        
        self.url = url


    @allure.step("API. Отправить поисковой запрос. Текст запроса: '{text}'")
    def search_among_all(self, text: str):
        """
        Функция отправляет поисковой запрос, в параметре 'text' указывается текст поискового запроса
        """
        variables = {"search": text, "cursor": "", "noMisspell": False}
        response = requests.post(self.url, json={"query": query_string, "variables": variables})
        return response
    

    @allure.step("API. Отправить поисковой запрос в определенном разделе. Раздел: '{}';Текст запроса: '{text}'")
    def search_in_section (self, text: str, section: str):
        """
        Функция отправляет поисковой запрос в определенном разделе, \n
        в параметре 'text' указывается текст поискового запроса,\n
        в параметре 'section' указывается название раздела
        """
        variables = {"search": text, "cursor": "","type": section, "noMisspell": False}
        response = requests.post(self.url, json={"query": query_string, "variables": variables})
        return response