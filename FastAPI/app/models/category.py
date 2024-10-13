from pydantic import BaseModel


class Category(BaseModel):
    id_category: int
    name: str
    description: str
