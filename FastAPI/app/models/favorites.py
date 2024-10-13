from pydantic import BaseModel


class Favorites(BaseModel):
    id_favorites: int
    id_user: int
    id_recipe: int
