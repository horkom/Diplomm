from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def find(self, locator: tuple) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator: tuple) -> None:
        """Надёжный клик: ждёт видимый элемент и кликает."""
        element = self.find_visible(locator)
        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator: tuple, text: str) -> None:
        element = self.find_visible(locator)
        element.click()
        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(text)

    def find_visible(self, locator: tuple) -> WebElement:
        """Дождаться появления хотя бы одного видимого элемента по локатору."""
        def _visible(driver):
            elements = driver.find_elements(*locator)
            for el in elements:
                if el.is_displayed():
                    return el
            return False
        return self.wait.until(_visible)
