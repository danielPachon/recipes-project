from pydantic import BaseModel


class Menu(BaseModel):
    id_menu: int
    name: str
    id_typeMenu: int
