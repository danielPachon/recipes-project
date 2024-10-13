from pydantic import BaseModel


class TypeMenu(BaseModel):
    id_typeMenu: int
    name: str
    type: str
