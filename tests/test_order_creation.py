import pytest
import requests
import allure
from api.api_order import *
from utils.utils import *
import api.locators as locators

@allure.feature("Изменение данных пользователя")
class TestOrderCreation:
    @allure.title("Создание заказа без авторизации")
    def test_get_order_unauthorized(self):
        response = OrderAPI.get_user_orders_unauth()
        assert response.status_code == 401
        assert response.json().get(locators.unauthorised, "false")

    @allure.title("Создание заказа без авторизации")
    def test_get_order_with_authorized(self):
        token = "valid_token"
        headers = {"Authorization": token}
        response = OrderAPI.get_user_orders(headers=headers)
        assert response.status_code == 200