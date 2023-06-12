import unittest

from Core.recipeProject import RecipeManager
from Core.recipeProject import Recipe

class TestRecipeManagerIntegration(unittest.TestCase):

    # tests basic functionalities
    # expected: the recipe will add then delete right after.
    def test_add_and_delete_recipe(self):
        rm = RecipeManager()
        new_recipe = Recipe(
            3,
            "Scrambled Eggs",
            "tyler",
            1,
            3,
            2,
            [
                {"ingredientName": "chicken eggs", "quantity": 3, "measurement": "pieces"},
                {"ingredientName": "milk", "quantity": 1, "measurement": "cup"},
                {"ingredientName": "butter", "quantity": 1, "measurement": "tbsp"},
            ],
            {
                "1": "Add the butter.",
                "2": "Add the beaten milk and eggs.",
            })

        rm.addRecipe(new_recipe)
        rm.deleteRecipe(new_recipe.id)

        self.assertNotIn(new_recipe, rm.data)

    # tests adding a recently deleted id
    # expected: addRecipe adds the recipe with the recently deleted id.
    def test_add_and_delete_recipe_RECENTLY_DELETED_ID(self):
        rm = RecipeManager()

        new_recipe_a = Recipe(
            3,
            "Scrambled Eggs",
            "tyler",
            1,
            3,
            2,
            [
                {"ingredientName": "chicken eggs", "quantity": 3, "measurement": "pieces"},
                {"ingredientName": "milk", "quantity": 1, "measurement": "cup"},
                {"ingredientName": "butter", "quantity": 1, "measurement": "tbsp"},
            ],
            {
                "1": "Add the butter.",
                "2": "Add the beaten milk and eggs.",
            })

        new_recipe_b = Recipe(
            3,
            "Fried Eggs",
            "cornelius",
            1,
            3,
            2,
            [
                {"ingredientName": "chicken eggs", "quantity": 3, "measurement": "pieces"},
                {"ingredientName": "butter", "quantity": 1, "measurement": "tbsp"},
            ],
            {
                "1": "Add the butter.",
                "2": "Add the eggs.",
            })

        rm.addRecipe(new_recipe_a)
        rm.deleteRecipe(new_recipe_a.id)
        rm.addRecipe(new_recipe_b)

        self.assertIn(new_recipe_b, rm.data)

if __name__ == "__main__":
    unittest.main()
