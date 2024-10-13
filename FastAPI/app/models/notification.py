from datetime import datetime
from pydantic import BaseModel


class Notification(BaseModel):
    id_notification: int
    message: str
    shopping_date: datetime
    id_user: int
