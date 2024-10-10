from config.stages import get_stage


class Endpoints:

    get_wishlist_by_uuid = lambda self, uuid: f"{get_stage()}/users/{uuid}/wishlist"


