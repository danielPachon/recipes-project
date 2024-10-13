from pydantic import BaseModel


class UserGroup(BaseModel):
    id_user: int
    id_group: int
