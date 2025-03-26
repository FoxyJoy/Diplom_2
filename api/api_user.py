import requests
import allure

class UserAPI:
    main_url = "https://stellarburgers.nomoreparties.site/api/auth"

    @staticmethod
    @allure.step("Создание пользователя")
    def create_user(name, email, password):
        payload = {
            "name": name,
            "email": email,
            "password": password
        }
        return requests.post(f"{UserAPI.main_url}/register", json=payload)

    @staticmethod
    @allure.step("Логинимся")
    def login_user(email, password):
        payload = {
            "email": email,
            "password": password
        }
        return requests.post(f"{UserAPI.main_url}/login", json=payload)

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(email, password):
        # Логинися, чтоб получить токен
        login_response = UserAPI.login_user(email, password)
        if login_response.status_code != 200:
            raise Exception("Не удалось войти для удаления пользователя")

        token = login_response.json().get('accessToken')
        headers = {'Authorization': f"Bearer {token}"}

        # Удаляем пользователя
        return requests.delete(f"{UserAPI.main_url}/user", headers=headers)

    @staticmethod
    @allure.step("Обновление данных пользователя")
    def update_user(headers=None, updated_data=None):
        url = f"{UserAPI.main_url}/user"
        return requests.patch(url, headers=headers, json=updated_data)