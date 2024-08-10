from pydantic import BaseModel


class RecipeCreate(BaseModel):
    title: str
    cook_time: int
    ingredients: str
    description: str
