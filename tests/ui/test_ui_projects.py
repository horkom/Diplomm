import allure
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config.config import UI_URL
from pages.login_page import LoginPage
from pages.project_page import ProjectPage


@allure.title("Вход в систему")
@allure.story("UI: авторизация")
@pytest.mark.ui
def test_login(driver) -> None:
    login_page = LoginPage(driver)
    with allure.step("Открыть страницу логина"):
        login_page.open()
    with allure.step("Выполнить вход"):
        login_page.login()
    with allure.step("Дождаться исчезновения формы логина"):
        WebDriverWait(driver, 15).until(
            EC.invisibility_of_element_located(login_page.PASSWORD_INPUT)
        )


@allure.title("Создание проекта")
@allure.story("UI: проекты")
@pytest.mark.ui
def test_create_project(driver) -> None:
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login()

    project_page = ProjectPage(driver)

    with allure.step("Создать проект 'Тестовый проект'"):
        project_page.create_project("Тестовый проект")

    with allure.step("Вернуться на страницу команды (список проектов)"):
        driver.get(UI_URL)
        # дождаться появления хотя бы одной карточки проекта
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(project_page.PROJECT_CARD)
        )

    with allure.step("Проверить, что проект появился в списке"):
        titles = project_page.get_all_project_titles()
        assert "Тестовый проект" in titles, (
            f"Проект не найден. Все проекты: {titles}"
        )
