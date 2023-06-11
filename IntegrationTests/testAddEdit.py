import unittest

from Core.recipeProject import RecipeManager


class TestRecipeManagerIntegration(unittest.TestCase):

    def test_add_and_update_recipe(self):
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

        # Test adding the new recipe
        rm.addRecipe(new_recipe)
        self.assertEqual(len(rm.data), 4)
        self.assertEqual(rm.data[-1]['recipeName'], "Alfredo Pasta")

        # Test updating the recipe
        updated = rm.updateRecipe(3, new_recipe_name="lemon chicken pasta", new_recipe_author="Samson",
                                  new_prep_time=6, new_cook_time=11, new_serving_size=3)
        self.assertTrue(updated)
        self.assertEqual(rm.data[-1]['recipeName'], "lemon chicken pasta")
        self.assertEqual(rm.data[-1]['recipeAuthor'], "Samson")
        self.assertEqual(rm.data[-1]['prepTime'], 6)
        self.assertEqual(rm.data[-1]['cookTime'], 11)
        self.assertEqual(rm.data[-1]['servingSize'], 3)


if __name__ == "__main__":
    unittest.main()
