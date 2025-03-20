import pytest
import requests
import allure
from api.api_user import *
from utils.utils import *
import api.locators as locators

@allure.feature("Логин пользователя")
class TestLoginUser:
    @allure.title('Пользователь может авторизоваться')
    def test_login_user_true(self):
        # Создаем пользователя
        name, email, password = register_new_user_and_return_login_password()

        # Выполняем вход с использованием данных
        login_response = UserAPI.login_user(email=email, password=password)

        # Проверяем, что вход выполнен успешно
        assert login_response.status_code == 200
        assert locators.accessToken in login_response.json()

    @allure.title('Для авторизации нужно передать все обязательные поля')
    def test_login_user_missing_fild(self):
        response = UserAPI.login_user("login_only", "")
        assert response.status_code == 401
        assert locators.email_or_pass_incorrect in response.text

    @allure.title('Система возвращает ошибку, если неправильно указать логин')
    def test_login_user_invalid_credentials(self):
        response = UserAPI.login_user("invalid_login", "valid_password")
        assert response.status_code == 401
        assert locators.email_or_pass_incorrect in response.text

    @allure.title('Система возвращает ошибку, если неправильно указать пароль')
    def test_password_user_invalid_credentials(self):
        response = UserAPI.login_user("valid_login", "invalid_password")
        assert response.status_code == 401
        assert locators.email_or_pass_incorrect in response.text
