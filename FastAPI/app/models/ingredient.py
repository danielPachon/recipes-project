from datetime import datetime
from pydantic import BaseModel


class Ingredient(BaseModel):
    id_ingredient: int
    name: str
    expiration_date: datetime
    id_nutrition_info: int
