from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class TaskPage(BasePage):
    # Локаторы
    CREATE_TASK_BUTTON = (
        By.XPATH,
        "//div[@role='button' and contains(., 'Добавить задачу')]",
    )
    TASK_TITLE_INPUT = (
        By.CSS_SELECTOR, "[data-testid='board-task-input-name']"
        )
    TASK_TITLE = (By.CSS_SELECTOR, "[data-testid='board-task-title']")
    TASK_DONE_TOGGLE = (By.CSS_SELECTOR, "[data-testid='task-done-toggle']")
    TASK_DONE_ICON = (By.CSS_SELECTOR, "[data-testid='task-done-toggle'] svg")

    # --- Действия ---
    def create_task(self, title: str) -> None:
        """Создать задачу."""
        self.click(self.CREATE_TASK_BUTTON)
        self.find(self.TASK_TITLE_INPUT)
        self.send_keys(self.TASK_TITLE_INPUT, title)
        self.find(self.TASK_TITLE_INPUT).send_keys(Keys.ENTER)

    def open_task(self) -> None:
        """Открыть первую задачу из списка."""
        self.click(self.TASK_TITLE)

    def mark_task_done(self) -> None:
        """Кликнуть по галочке «Готово»."""
        self.click(self.TASK_DONE_TOGGLE)

    # --- Проверки ---
    def get_all_task_titles(self) -> list[str]:
        """Вернуть список названий всех задач в текущем проекте."""
        self.wait.until(
            EC.presence_of_all_elements_located(self.TASK_TITLE)
        )
        elements = self.driver.find_elements(*self.TASK_TITLE)
        return [el.text for el in elements]

    def is_task_present(self, title: str) -> bool:
        """Проверить, есть ли задача с указанным названием."""
        return title in self.get_all_task_titles()

    def get_done_icon_name(self) -> str:
        """Вернуть имя иконки статуса (data-icon)."""
        return self.find(self.TASK_DONE_ICON).get_attribute("data-icon")
