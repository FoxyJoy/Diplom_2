import pytest
import requests
import allure
from api.api_order import *
from utils.utils import *
import api.locators as locators

@allure.feature("Создание заказа")
class TestUserOrders:
    @allure.title("Создание заказа с авторизацией")
    def test_get_orders_authorized(self):
        token = "valid_token"
        headers = {"Authorization": token}
        response = OrderAPI.get_user_orders_ingredients(ingredients=locators.ingredients_in_order, headers=headers)
        response_data = response.json()
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert "order" in response_data  # Проверяем наличие ключа order в ответе
        assert isinstance(response_data["order"], dict)  # Проверяем тип данных order

    @allure.title("Создание заказа без авторизации")
    def test_get_orders_unauthorized(self):
        # Используем метод из OrderAPI без заголовков
        response = OrderAPI.get_user_orders_unauth(ingredients=locators.ingredients_unauthorized)
        assert response.status_code == 401
        assert response.json().get(locators.unauthorised, "false")

    @allure.title("Создание заказа с невалидным ингредиентом")
    def test_get_orders_without_ingredients(self):
        token = "valid_token"
        headers = {"Authorization": token}
        response = OrderAPI.create_order(ingredients=locators.invalid_ingredient, headers=headers)
        assert response.status_code == 404

    @allure.title("Создание заказа без ингредиентов")
    def test_get_orders_without_ingredients(self):
        token = "valid_token"
        headers = {"Authorization": token}
        invalid_ingredient = None
        response = OrderAPI.get_user_orders_without_ingredients(ingredients=invalid_ingredient, headers=headers)
        assert response.status_code == 400
        assert response.json().get(locators.ingred_proided, "false")

    @allure.title("Создание заказа с некорректным хешем")
    def test_get_orders_without_ingredients(self):
        token = "valid_token"
        headers = {"Authorization": token}
        response = OrderAPI.get_order_invalid_ingredient_hash(headers=headers, ingredients=locators.ingredient)
        assert response.status_code == 500
        assert locators.server_error in response.text

    @allure.title("Создание заказа с ингредиентами")
    def test_get_orders_with_ingredients(self):
        token = "valid_token"
        headers = {"Authorization": token}
        response = OrderAPI.get_user_orders_ingredients(ingredients=locators.ingredients_in_order, headers=headers)
        assert response.status_code == 200
        assert "order" in response.json()















