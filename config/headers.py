import os
from dotenv import load_dotenv

def get_token():
    ...
    os.environ["TOKEN"] = ...

get_token()

class Headers:

    # def basic(self, xtaskid="api-research"):
    #     return {
    #         "Authorization": f"Bearer {os.getenv('TOKEN')}",
    #         "X-Task-Id": xtaskid,
    #         "X-Request-ID": ...
    #     }

    basic = {
        "Authorization": f"Bearer {os.getenv('TOKEN')}",
        "X-Task-Id": "api-research"
    }
