import allure
import requests
from config.headers import Headers
from services.wishlists.payloads import Payloads
from services.wishlists.endpoints import Endpoints

from utils.helper import Helper
from services.wishlists.models.wishlist_model import CatalogResponseModel


class WishlistsAPI(Helper):

    def __init__(self):
        self._headers = Headers()
        self._payloads = Payloads()
        self._endpoints = Endpoints()

    @allure.step("Get wishlist by user uuid")
    def get_wishlist_by_uuid(self, uuid):
        response = requests.get(
            url=self._endpoints.get_wishlist_by_uuid(uuid),
            headers=self._headers.basic
        )
        self.attach_response(response.json())
        assert response.status_code == 200, response.json()
        model = CatalogResponseModel(**response.json())
        return model