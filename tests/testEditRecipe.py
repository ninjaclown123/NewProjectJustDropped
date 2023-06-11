import unittest

from Core.recipeProject import RecipeManager


class TestRecipeManagement(unittest.TestCase):

    def setUp(self):
        self.recipe = RecipeManager()
        self.recipe.data = [
            {
                "id": "1",
                "recipeName": "Pizza",
                "recipeAuthor": "John Doe",
                "prepTime": 20,
                "cookTime": 15,
                "servingSize": 4,
                "ingredients": ["dough", "tomato sauce", "cheese"],
                "instructions": ["Roll out dough", "Add sauce and cheese", "Bake"]
            }
        ]

    def test_update_existing_recipe(self):
        # Test updating an existing recipe with valid data
        update_result = self.recipe.updateRecipe("1", new_recipe_name="Pasta")
        self.assertTrue(update_result)
        self.assertEqual(self.recipe.data[0]["recipeName"], "Pasta")

    def test_update_nonexistent_recipe(self):
        # Test updating a non-existent recipe
        update_result = self.recipe.updateRecipe("2", new_recipe_name="Pasta")
        self.assertFalse(update_result)

    def test_update_partial_data(self):
        # Test updating an existing recipe with only some of the data provided
        update_result = self.recipe.updateRecipe("1", new_recipe_name="Pasta", new_cook_time=25)
        self.assertTrue(update_result)
        self.assertEqual(self.recipe.data[0]["recipeName"], "Pasta")
        self.assertEqual(self.recipe.data[0]["cookTime"], 25)
        self.assertEqual(self.recipe.data[0]["prepTime"], 20)  # Should remain unchanged

    def test_update_no_data(self):
        # Test updating an existing recipe without providing any new data
        update_result = self.recipe.updateRecipe("1")
        self.assertTrue(update_result)
        self.assertEqual(self.recipe.data[0]["recipeName"], "Pizza")  # Should remain unchanged


if __name__ == '__main__':
    unittest.main()
