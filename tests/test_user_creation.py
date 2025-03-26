import pytest
import requests
import allure
from utils.utils import *
import api.locators as locators

@allure.feature("Создание пользователя")
class TestUserCreation:
    @allure.title("Создать уникального пользователя")
    def test_create_unique_user(self):
        user_data = register_new_user_and_return_login_password()
        assert len(user_data) == 3  # Список данных пользователя должен содержать 3 элемента (логин, пароль, имя)

    @allure.title("Создать уже зарегистрированного пользователя")
    def test_create_already_registered_user(self):
        # Используем функцию для создания пользователя
        name, email, password = register_new_user_and_return_login_password()

        # Пытаемся создать пользователя с теми же данными
        create_response = UserAPI.create_user(name=name, email=email, password=password)
        assert create_response.status_code == 403
        assert create_response.json().get("message", "")

    @allure.title('Для регистрации нужно передать все обязательные поля')
    def test_create_user_missing_fild(self):
        response = UserAPI.create_user("login_only", "", "password_only")
        assert response.status_code == 403
        assert locators.user_missing_fild in response.text


