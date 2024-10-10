from pydantic import BaseModel, UUID4, Field
from typing import List

class ProductItem(BaseModel):
    category_uuids: list
    price: int
    title: str
    uuid: UUID4

class CatalogResponseModel(BaseModel):
    items: List[ProductItem]
    user_uuid: UUID4

