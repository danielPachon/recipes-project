from pydantic import BaseModel


class User(BaseModel):
    id_user: int
    username: str
    name: str
    lastname: str
    email: str
    password: str
    profile_picture: str
    type_user: str
