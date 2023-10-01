"""Page Object Model for Search Page"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class SearchPage:
    """Страница результата поиска"""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self) -> None:
        """Открыть страницу корзины"""
        self.driver.get(
            "https://tutorialsninja.com/demo/index.php?route=product/search"
        )

    def set_search_query(self, query: str) -> None:
        """Ввести ключевое слово в поле поиска"""
        self.driver.find_element(By.NAME, "search").send_keys(query)

    def click_search(self) -> None:
        """Нажать кнопку поиска"""
        self.driver.find_element(By.CSS_SELECTOR, "button.btn-default").click()

    def search_criteria(self, query: str) -> None:
        """Ввести ключевое слово в поле поиска критерия"""
        self.driver.find_element(
            By.XPATH, "//input[@placeholder='Keywords']"
        ).send_keys(query)

    def click_search_criteria_button(self) -> None:
        """Нажать кнопку поиска критерия"""
        self.driver.find_element(By.ID, "button-search").click()
