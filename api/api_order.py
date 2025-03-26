import requests
import allure

class OrderAPI:
    main_url = "https://stellarburgers.nomoreparties.site/api"

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(headers=None, ingredients=None):
        url = f"{OrderAPI.main_url}/auth/orders"
        data = {"ingredients": ingredients} if ingredients else {}
        return requests.post(url, headers=headers, json=data)

    @staticmethod
    @allure.step("Получение заказов пользователя")
    def get_user_orders(headers=None):
        url = f"{OrderAPI.main_url}/auth/orders"
        return requests.get(url, headers=headers)

    @staticmethod
    @allure.step("Получение заказов пользователя без авторизации")
    def get_user_orders_unauth(ingredients=None):
        url = f"{OrderAPI.main_url}/orders"
        params = {"ingredients": ingredients} if ingredients else {}
        return requests.get(url, params=params)

    @staticmethod
    @allure.step("Получение заказов пользователя без ингредиентов")
    def get_user_orders_without_ingredients(headers=None, ingredients=None):
        url = f"{OrderAPI.main_url}/orders"
        data = {"": ingredients} if ingredients else {}
        return requests.post(url, headers=headers, json=data)

    @staticmethod
    @allure.step("Получение заказов c неверным хешом ингредиента")
    def get_order_invalid_ingredient_hash(headers=None, ingredients=None):
        url = f"{OrderAPI.main_url}/orders"
        data = {"ingredients": ingredients} if ingredients else {}
        return requests.post(url, headers=headers, json=data)

    @staticmethod
    @allure.step("Получение заказов пользователя с ингредиентами")
    def get_user_orders_ingredients(headers=None, ingredients=None):
        url = f"{OrderAPI.main_url}/orders"
        data = {"ingredients": ingredients} if ingredients else {}
        return requests.post(url, headers=headers, json=data)





