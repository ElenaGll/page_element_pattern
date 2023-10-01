from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_element import PageElement


class HomePage:
    """Домашняя страница сайта https://tutorialsninja.com/demo/"""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.search_field = PageElement(self.driver, (By.NAME, "search"))
        self.search_button = PageElement(
            self.driver, (By.CSS_SELECTOR, "button.btn-default")
        )
        self.shopping_cart = PageElement(
            self.driver, (By.CSS_SELECTOR, "button.btn-inverse")
        )
        self.shopping_cart_menu = PageElement(
            self.driver, (By.LINK_TEXT, "Shopping Cart")
        )

    def open(self) -> None:
        """Открыть главную страницу сайта"""
        self.driver.get("https://tutorialsninja.com/demo/")

    def set_search_query(self, query: str) -> None:
        """Ввести ключевое слово в поле поиска"""
        self.search_field.send_keys(query)

    def click_search(self) -> None:
        """Нажать кнопку поиска"""
        self.search_button.click()

    def click_shopping_cart_button(self) -> None:
        """Нажать на кнопку корзины"""
        self.shopping_cart.click()

    def click_shopping_cart_menu(self) -> None:
        """Перейти на страницу корзины"""
        self.shopping_cart_menu.click()
