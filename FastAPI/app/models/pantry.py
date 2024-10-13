from datetime import datetime
from pydantic import BaseModel


class Pantry(BaseModel):
    id_pantry: int
    id_ingredient: int
    id_user: int
    id_quantity: int
    expiration_date: datetime
