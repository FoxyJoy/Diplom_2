import requests
import random
import string
import allure
import pytest
from api.api_user import UserAPI

@allure.step("генерация")
def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

@allure.step("Сначала создаем пользователя")
def register_new_user_and_return_login_password():
    user_pass = []
    name = generate_random_string(10)
    password = generate_random_string(10)
    email = f"{generate_random_string(10)}@example.com"

    # Cоздаем пользователя через API
    # response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=payload)
    response = UserAPI.create_user(name=name, email=email,password=password)

    if response.status_code == 200:
        return name, email, password
    else:
        raise Exception(f"Не удалось создать пользователя: {response.status_code}, {response.text}")


@allure.step("Сначала создаем пользователя, чтобы потом его удалить из базы")
@pytest.fixture
def create_and_delete_user():
    # Создаем пользователя и получаем его данные
    user_data = register_new_user_and_return_login_password()
    yield user_data  # Передаем данные в тест

    # Удаляем пользователя после завершения теста
    email, password, _ = user_data
    UserAPI.delete_user(email=email, password=password)

