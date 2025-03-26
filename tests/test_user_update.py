import pytest
import requests
import allure
from api.api_user import *

@allure.feature("Обновление пользователя")
class TestChangingUserData:
    @allure.title("Изменение данных пользователя с авторизацией")
    def test_update_user_authorized(self):
        # Предположим, что у нас есть валидный токен
        token = "valid_token"
        headers = {"Authorization": token}
        update_data = {"name": "Updated Name"}
        response = UserAPI.update_user(headers=headers, updated_data=update_data)
        assert response.json().get("message", "true")

    @allure.title("Изменение данных пользователя без авторизации")
    def test_update_user_unauthorized(self):
        update_data = {"name": "Updated Name"}
        # Используем метод из UserAPI без заголовков
        response = UserAPI.update_user(updated_data=update_data)
        assert response.status_code == 401