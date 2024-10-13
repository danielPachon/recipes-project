from pydantic import BaseModel


class Quantity(BaseModel):
    id_quantity: int
    grammes: float
    liters: float
