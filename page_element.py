"""Page element implementation"""
from typing import Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class PageElement:
    """Класс для основных команд"""

    def __init__(self, driver: WebDriver, locator: Tuple[str, str]):
        self.driver = driver
        self.locator = locator

    def get_element(self) -> WebElement:
        """Получить элемент"""
        return self.driver.find_element(*self.locator)

    def click(self) -> None:
        """Сделать клип по кнопке"""
        self.driver.find_element(*self.locator).click()

    def send_keys(self, query: str) -> None:
        """Написать запрос в поле поиска"""
        self.driver.find_element(*self.locator).send_keys(query)
