from datetime import time
from pydantic import BaseModel


class Recipe(BaseModel):
    id_recipe: int
    name: str
    description: str
    instructions: str
    preparation_time: time
    status: bool
    difficulty: int
    id_ingredient: int
    id_user: int
    id_quantity: int
