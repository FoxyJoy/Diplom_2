## Дипломный проект. Задание 2: API-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы API-тесты, покрывающие классы `TestOrderCreation`, `TestLoginUser`, `TestUserCreation`, `TestUserOrders`, `TestChangingUserData`

В связи с грядущим релизом были созданы проверки: 

### Структура проекта
#### В директории В директории [utils](utils) лежат требуемые для тестов [Тестовые данные user-a][utils](utils/utils.py).

#### В директории [api](api) лежат actions [для "Тестирования юзера"](api/api_user.py), [для "Создания заказа"](api/api_order.py), [для "Локаторов"](api/locators.py).



### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=praktikum --cov-report=html`

