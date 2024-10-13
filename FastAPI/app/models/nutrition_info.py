from pydantic import BaseModel


class NutritionInfo(BaseModel):
    id_nutrition_info: int
    sugar: float
    calories: float
    protein: float
    fat: float
    carbohydrates: float
