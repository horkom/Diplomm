import allure
import pytest
from pages.task_page import TaskPage


@allure.title("Создание задачи")
@allure.story("UI: задачи")
@pytest.mark.ui
def test_create_task(logged_in) -> None:
    task_page = TaskPage(logged_in)
    with allure.step("Создать задачу 'Тестовая задача'"):
        task_page.create_task("Тестовая задача")


@allure.title("Создание задачи с длинным названием")
@allure.story("UI: задачи")
@pytest.mark.ui
def test_create_task_with_long_title(logged_in) -> None:
    task_page = TaskPage(logged_in)
    long_title = (
        "ОченьДлинноеНазваниеЗадачиКотороеПроверяет"
        "ЧтоИнтерфейсКорректноОбрабатываетДлинныйТекст_777"
    )
    with allure.step("Создать задачу с длинным названием"):
        task_page.create_task(long_title)


@allure.title("Новая задача создаётся со статусом «не выполнена»")
@allure.story("UI: задачи")
@pytest.mark.ui
def test_task_default_status(logged_in) -> None:
    task_page = TaskPage(logged_in)
    with allure.step("Создать задачу"):
        task_page.create_task("Задача_статус_777")
    with allure.step("Открыть задачу в правой панели"):
        task_page.open_task()
    with allure.step("Проверить, что статус «не выполнена»"):
        assert task_page.get_done_icon_name() == "IconCustomTaskDoneEmpty"
