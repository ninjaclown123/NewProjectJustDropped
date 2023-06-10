import unittest
from Core.recipeProject import RecipeManager


class TestRecipeManagement(unittest.TestCase):
    def setUp(self):
        self.rm = RecipeManager()

    def test_update_recipe_valid_id(self):
        # Case: Update recipe with valid ID and check if the returned value is True
        result = self.rm.updateRecipe(
            id=1,
            new_recipe_name="Vegan Bolognese",
            new_recipe_author="Jane Doe",
            new_prep_time=25,
            new_cook_time=40,
            new_serving_size=5
        )
        self.assertTrue(result)

        # Verify that the recipe was indeed updated
        recipe = next((recipe for recipe in self.rm.data if recipe["id"] == 1), None)
        self.assertIsNotNone(recipe)
        self.assertEqual(recipe["recipeName"], "Vegan Bolognese")
        self.assertEqual(recipe["recipeAuthor"], "Jane Doe")
        self.assertEqual(recipe["prepTime"], 25)
        self.assertEqual(recipe["cookTime"], 40)
        self.assertEqual(recipe["servingSize"], 5)

    def test_update_recipe_invalid_id(self):
        # Case: Attempt to update recipe with invalid ID and check if the returned value is False
        result = self.rm.updateRecipe(
            id=100,  # This ID does not exist
            new_recipe_name="Vegan Bolognese",
            new_recipe_author="Jane Doe",
            new_prep_time=25,
            new_cook_time=40,
            new_serving_size=5
        )
        self.assertFalse(result)

    def test_update_recipe_no_changes(self):
        # Case: Call updateRecipe with valid ID but without providing any new values,
        # check if the returned value is True and the recipe is unchanged
        recipe_before_update = next((recipe for recipe in self.rm.data if recipe["id"] == 2), None)
        result = self.rm.updateRecipe(id=2)
        self.assertTrue(result)

        # Verify that the recipe was not changed
        recipe_after_update = next((recipe for recipe in self.rm.data if recipe["id"] == 2), None)
        self.assertEqual(recipe_before_update, recipe_after_update)


if __name__ == '__main__':
    unittest.main()
