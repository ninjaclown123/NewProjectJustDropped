import unittest

from Core.recipeProject import RecipeManager
from Core.recipeProject import Recipe

class TestRecipeManagerIntegration(unittest.TestCase):

    # tests basic functionalities
    # expected: the view recipe returns the newly added recipe.
    def test_add_and_view_specific_recipe(self):
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
        my_recipe = rm.viewSpecificRecipe(new_recipe.id)

        self.assertEqual(new_recipe, my_recipe)
        self.assertEqual(new_recipe.recipe_author, my_recipe.recipe_author)
        self.assertEqual(new_recipe.instructions["1"], my_recipe.instructions["1"])

if __name__ == "__main__":
    unittest.main()
