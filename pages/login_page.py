from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import UI_URL, UI_LOGIN, UI_PASSWORD


class LoginPage(BasePage):
    # Поля формы логина (проверено в DevTools)
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")

    # Кнопка «Войти» — это div с role="button", не <button>
    SUBMIT_BUTTON = (
        By.XPATH,
        "//div[@role='button' and contains(., 'Войти')]"
    )

    def open(self) -> None:
        self.driver.get(UI_URL)

    def login(
        self,
        email: str = UI_LOGIN,
        password: str = UI_PASSWORD,
    ) -> None:
        self.send_keys(self.EMAIL_INPUT, email)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)
