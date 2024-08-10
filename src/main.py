from fastapi import FastAPI, HTTPException
from database import session, Recipe
import schemas


app = FastAPI()


@app.post("/recipes/")
async def create_recipe(recipe: schemas.RecipeCreate):
    db_recipe = Recipe(**recipe.dict())
    session.add(db_recipe)
    session.commit()
    session.refresh(db_recipe)
    session.close()
    return db_recipe


@app.get("/recipes/")
async def get_recipes():
    recipes = (
        session.query(Recipe).order_by(Recipe.views.desc(), Recipe.cook_time).all()
    )
    session.close()
    return recipes


@app.get("/recipes/{recipe_id}")
async def get_recipe(recipe_id: int):
    recipe = session.query(Recipe).filter(Recipe.id == recipe_id).first()
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    recipe.views += 1
    session.commit()
    return {
        "title": recipe.title,
        "cook_time": recipe.cook_time,
        "ingredients": recipe.ingredients,
        "description": recipe.description,
    }