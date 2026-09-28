from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProjectPage(BasePage):
    # --- Локаторы ---
    CREATE_PROJECT_BUTTON = (
        By.CSS_SELECTOR, "[data-testid='add-project-card']"
        )
    DEFAULT_PROJECT_ITEM = (
        By.CSS_SELECTOR,
        "[data-testid='menu-item-add-default-project']",
    )
    PROJECT_TITLE_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='Введите название проекта…']",
    )
    SAVE_BUTTON = (
        By.XPATH,
        "//div[@role='button' and contains(., 'Добавить проект с задачами')]",
    )
    PROJECT_CARD = (By.CSS_SELECTOR, "[data-testid='project-card']")
    PROJECT_TITLE = (By.CSS_SELECTOR, "[data-testid='project-title']")

    # --- Методы ---
    def open_create_form(self) -> None:
        """Открыть форму создания проекта."""
        self.click(self.CREATE_PROJECT_BUTTON)
        self.click(self.DEFAULT_PROJECT_ITEM)

    def create_project(self, title: str) -> None:
        """Создать проект с указанным названием."""
        self.open_create_form()
        self.send_keys(self.PROJECT_TITLE_INPUT, title)
        self.click(self.SAVE_BUTTON)

    def get_all_project_titles(self) -> list[str]:
        """Вернуть список названий всех проектов."""
        self.wait.until(
            EC.presence_of_all_elements_located(self.PROJECT_TITLE)
        )
        elements = self.driver.find_elements(*self.PROJECT_TITLE)
        return [el.text for el in elements]

    def is_project_present(self, title: str) -> bool:
        """Проверить, есть ли проект с указанным названием."""
        return title in self.get_all_project_titles()

    # 👇 ВОТ ЭТОТ МЕТОД — добавьте его в конец класса
    def open_first_project(self) -> None:
        """Открыть первый проект из списка."""
        cards = self.wait.until(
            EC.presence_of_all_elements_located(self.PROJECT_CARD)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", cards[0]
        )
        cards[0].click()
