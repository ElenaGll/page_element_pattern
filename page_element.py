from typing import Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class PageElement:

    def __init__(self, driver: WebDriver, locator: Tuple[str, str]):
        self.driver = driver
        self.locator = locator

    def get_element(self) -> WebElement:
        return self.driver.find_element(*self.locator)

    def click(self) -> None:
        self.driver.find_element(*self.locator).click()

    def send_keys(self, query: str) -> None:
        self.driver.find_element(*self.locator).send_keys(query)

