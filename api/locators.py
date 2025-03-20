import pytest

unauthorised = 'You should be authorised'  # Запрос без авторизации 401
ingred_proided = 'Ingredient ids must be provided'# Если не передать ни один ингредиент, вернётся код ответа 400 Bad Request. Создание заказа
server_error = 'Internal Server Error'  # в запросе передан невалидный хеш ингредиента, вернётся код ответа 500
ingredient = ["Флюоресцентная булка R2-D3", "Флюоресцентная булка R2-D3"]
ingredients_unauthorized = ["ingredients1", "ingredients2"]
invalid_ingredient = ["invalid_ingredient"]
ingredients_in_order = ["61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa70"]
user_missing_fild = 'Email, password and name are required fields' # Для регистрации нужно передать все обязательные поля
accessToken = 'accessToken' # токен используют в запросах к эндпоинту auth/user
email_or_pass_incorrect = 'email or password are incorrect' # Если логин или пароль неверные или нет одного из полей, вернётся код ответа 401 Unauthorized.
