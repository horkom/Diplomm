# Diplom

Дипломный проект по автоматизации тестирования веб-приложения [YouGile](https://ru.yougile.com/).

## Стек
- Python 3.13
- pytest
- Selenium (UI)
- Requests (API)
- Allure (отчёты)

## Установка

```bash
pip install -r requirements.txt

Запуск тестов:

# Все тесты
pytest --alluredir=allure-results

# Только UI
pytest -m ui --alluredir=allure-results

# Только API
pytest -m api --alluredir=allure-results

Отчёт Allure:

allure serve allure-results

Структура проекта:

├── api/           # API-клиент
├── config/        # Конфигурация (.env)
├── pages/         # Page Object для UI-тестов
├── tests/
│   ├── api/       # API-тесты (5 шт)
│   └── ui/        # UI-тесты (5 шт)
├── conftest.py    # Фикстуры
├── pytest.ini     # Настройки pytest
└── requirements.txt
