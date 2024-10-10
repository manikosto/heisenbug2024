from services.users.api_users import UsersAPI
from services.wishlists.api_wishlists import WishlistsAPI
class BaseTest:

    def setup_method(self):
        self.api_users = UsersAPI()
        self.api_wishlists = WishlistsAPI()