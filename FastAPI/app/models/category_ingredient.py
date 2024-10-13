from pydantic import BaseModel


class CategoryIngredient(BaseModel):
    id_category_ingredient: int
    id_ingredient: int
    id_category: int
