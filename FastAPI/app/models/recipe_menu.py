from pydantic import BaseModel


class RecipeMenu(BaseModel):
    id_recipe: int
    id_menu: int
