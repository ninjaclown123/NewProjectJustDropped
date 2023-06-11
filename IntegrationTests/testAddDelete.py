import unittest

from Core.recipeProject import RecipeManager


class TestRecipeManagerIntegration(unittest.TestCase):

    # tests basic functionalities
    # expected: the recipe will add then delete right after.
    def test_add_and_delete_recipe(self):
        rm = RecipeManager()
        new_recipe = {
            "id": 3,
            "recipeName": "Alfredo Pasta",
            "recipeAuthor": "seiffdene",
            "prepTime": 5,
            "cookTime": 10,
            "servingSize": 2,
            "ingredients": [
                {"ingredientName": "chicken", "quantity": 1, "measurement": "kg"},
                {"ingredientName": "alfredo sauce", "quantity": 2, "measurement": "ounce"},
            ],
            "instructions": {
                "1": "Add the chicken.",
                "2": "Add the alfredo sauce.",
            }
        }

        rm.addRecipe(new_recipe)
        rm.deleteRecipe(new_recipe["id"])

        self.assertNotIn(new_recipe, rm.data)

    # tests adding a recently deleted id
    # expected: addRecipe adds the recipe with the recently deleted id.
    def test_add_and_delete_recipe_RECENTLY_DELETED_ID(self):
        rm = RecipeManager()

        new_recipe_a = {
            "id": 3,
            "recipeName": "Scrambled Eggs",
            "recipeAuthor": "tyler",
            "prepTime": 1,
            "cookTime": 3,
            "servingSize": 2,
            "ingredients": [
                {"ingredientName": "chicken eggs", "quantity": 3, "measurement": "pieces"},
                {"ingredientName": "milk", "quantity": 1, "measurement": "cup"},
                {"ingredientName": "butter", "quantity": 1, "measurement": "tbsp"},
            ],
            "instructions": {
                "1": "Add the butter.",
                "2": "Add the beaten milk and eggs.",
            }
        }

        new_recipe_b = {
            "id": 3,
            "recipeName": "Fried Eggs",
            "recipeAuthor": "tyler",
            "prepTime": 1,
            "cookTime": 3,
            "servingSize": 2,
            "ingredients": [
                {"ingredientName": "chicken eggs", "quantity": 3, "measurement": "pieces"},
                {"ingredientName": "butter", "quantity": 1, "measurement": "tbsp"},
            ],
            "instructions": {
                "1": "Add the butter.",
                "2": "Add the eggs.",
            }
        }

        rm.addRecipe(new_recipe_a)
        rm.deleteRecipe(new_recipe_a["id"])
        rm.addRecipe(new_recipe_b)

        self.assertIn(new_recipe_b, rm.data)

if __name__ == "__main__":
    unittest.main()
