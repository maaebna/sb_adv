from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_recipe():
    recipe_data = {
        "title": "Test Recipe",
        "cook_time": 30,
        "ingredients": "Ingredient 1, Ingredient 2",
        "description": "Test recipe description",
    }
    response = client.post("/recipes/", json=recipe_data)
    assert response.status_code == 200
    assert response.json()["title"] == recipe_data["title"]
    assert response.json()["cook_time"] == recipe_data["cook_time"]
    assert response.json()["ingredients"] == recipe_data["ingredients"]
    assert response.json()["description"] == recipe_data["description"]


def test_get_recipes():
    response = client.get("/recipes/")
    assert response.status_code == 200
    assert len(response.json()) >= 0


def test_get_recipe():
    detail_response = client.get("/recipes/0")
    assert detail_response.status_code == 200
