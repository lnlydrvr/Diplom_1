## Дипломный проект. Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `src` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты, разделенные по классам
- `htmlcov` - пакет, содержащий отчет о покрытии тестами кода программы
- `conftest.py` - файл, содержащий фикстуры к тестам
- `requirements.txt` - файл, содержащий зависимости к проекту

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=src --cov-report=html`
