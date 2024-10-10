import allure
import pytest
from config.base_test import BaseTest

@allure.epic("Heisenbug 2024 - Users API")
class TestExample(BaseTest):

    @allure.title("Create a new user")
    @pytest.mark.parametrize("email, expected_result", [
        ("qwe313122@ya.ru", True),
        ("qwerqwe.ru", False)
    ])
    def test_create_new_user(self, email, expected_result):
        user = self.api_users.create_user(email, expected_result)
        # self.api_wishlists.get_wishlist_by_uuid(user.uuid)