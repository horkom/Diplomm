import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.project_page import ProjectPage


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )
    yield driver
    driver.quit()


@pytest.fixture
def logged_in(driver):
    """Логин в YouGile + открытие первого проекта (клик по карточке)."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login()

    project_page = ProjectPage(driver)
    project_page.open_first_project()

    # Дождаться, что мы действительно на доске проекта
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH,
             "//div[@role='button' and contains(., 'Добавить задачу')]")
        )
    )
    return driver
