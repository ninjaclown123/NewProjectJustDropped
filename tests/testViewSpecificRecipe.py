import unittest

from Core.recipeProject import RecipeManager, Recipe


class TestRecipeManagement(unittest.TestCase):

    def setUp(self):
        self.rm = RecipeManager()
        # Add some sample recipes for testing
        recipe1 = Recipe(
            10,
            "Pancakes",
            "John",
            10,
            15,
            4,
            [
                {"ingredientName": "flour", "quantity": 1.5, "measurement": "cups"},
                {"ingredientName": "milk", "quantity": 1, "measurement": "cup"},
                {"ingredientName": "eggs", "quantity": 2, "measurement": "units"},
                {"ingredientName": "sugar", "quantity": 2, "measurement": "tablespoons"},
                {"ingredientName": "baking powder", "quantity": 2, "measurement": "teaspoons"},
                {"ingredientName": "salt", "quantity": 1, "measurement": "teaspoon"},
                {"ingredientName": "butter", "quantity": 2, "measurement": "tablespoons"}
            ],
            {
                "1": "In a large bowl, whisk together the flour, sugar, baking powder, and salt.",
                "2": "In a separate bowl, whisk together the milk, eggs, and melted butter.",
                "3": "Pour the wet ingredients into the dry ingredients and stir until just combined.",
                "4": "Heat a lightly greased griddle or frying pan over medium heat.",
                "5": "Pour 1/4 cup of batter onto the griddle for each pancake.",
                "6": "Cook until bubbles form on the surface, then flip and cook until golden brown."
            }
        )
        self.rm.addRecipe(recipe1)

    def test_viewSpecificRecipe_existingID(self):
        recipe = self.rm.viewSpecificRecipe(10)
        self.assertIsNotNone(recipe)
        self.assertEqual(recipe.recipe_name, "Pancakes")
        self.assertEqual(recipe.recipe_author, "John")

    def test_viewSpecificRecipe_nonexistentID(self):
        rm = RecipeManager()
        with self.assertRaises(ValueError):
            rm.viewSpecificRecipe(20)


if __name__ == "__main__":
    unittest.main()
