from pydantic import BaseModel


class RecipeCategory(BaseModel):
    id_recipe: int
    id_category: int
