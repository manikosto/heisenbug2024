import allure
import requests
from config.headers import Headers
from services.users.payloads import Payloads
from services.users.endpoints import Endpoints

from utils.helper import Helper
from services.users.models.user_model import UserModel

class UsersAPI(Helper):

    def __init__(self):
        self._headers = Headers()
        self._payloads = Payloads()
        self._endpoints = Endpoints()

    @allure.step("Create a new user")
    def create_user(self, email, expected_result):
        response = requests.post(
            url=self._endpoints.create_user,
            headers=self._headers.basic,
            json=self._payloads.create_user(email)
        )
        self.attach_response(response.json())
        if expected_result:
            assert response.status_code == 200, response.json()
            model = UserModel(**response.json())
            return model
        else:
            assert response.status_code != 200
            return response.json()