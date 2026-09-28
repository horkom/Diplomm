import allure
import pytest
from api.client import ApiClient


@allure.title("Получение списка компаний")
@allure.story("API: компании")
@pytest.mark.api
def test_get_companies() -> None:
    client = ApiClient()
    with allure.step("Отправить GET /companies"):
        response = client.get("/companies")
    with allure.step("Проверить статус-код 200"):
        assert response.status_code == 200


@allure.title("Получение списка проектов")
@allure.story("API: проекты")
@pytest.mark.api
def test_get_projects() -> None:
    client = ApiClient()
    with allure.step("Отправить GET /projects"):
        response = client.get("/projects")
    with allure.step("Проверить статус-код 200"):
        assert response.status_code == 200


@allure.title("Создание проекта")
@allure.story("API: проекты")
@pytest.mark.api
def test_create_project() -> None:
    client = ApiClient()
    payload = {"title": "Новый проект"}
    with allure.step("Отправить POST /projects"):
        response = client.post("/projects", json=payload)
    with allure.step("Проверить статус-код 201"):
        assert response.status_code == 201


@allure.title("Создание проекта без названия")
@allure.story("API: проекты")
@pytest.mark.api
def test_create_project_without_title() -> None:
    client = ApiClient()
    payload = {}
    with allure.step("Отправить POST /projects без title"):
        response = client.post("/projects", json=payload)
    with allure.step("Проверить статус-код 400"):
        assert response.status_code == 400


@allure.title("Получение проектов с невалидным токеном")
@allure.story("API: проекты")
@pytest.mark.api
def test_get_projects_invalid_token() -> None:
    client = ApiClient()
    client.headers["Authorization"] = "Bearer invalid_token"
    with allure.step("Отправить GET /projects с неверным токеном"):
        response = client.get("/projects")
    with allure.step("Проверить статус-код 401"):
        assert response.status_code == 401
