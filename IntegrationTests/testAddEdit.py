import unittest
from Core.recipeProject import RecipeManager, Recipe


class TestRecipeManagerIntegration(unittest.TestCase):

    def setUp(self):
        self.recipe_manager = RecipeManager()

    def test_addRecipe_and_editRecipe(self):
        # Create a new recipe
        new_recipe = Recipe(
            3,
            "New Recipe",
            "John",
            30,
            45,
            2,
            [
                {"ingredientName": "ingredient1", "quantity": 1, "measurement": "unit"},
                {"ingredientName": "ingredient2", "quantity": 2, "measurement": "units"}
            ],
            {"1": "Step 1", "2": "Step 2"}
        )

        # Add the recipe to the recipe manager
        self.recipe_manager.addRecipe(new_recipe)

        # Retrieve the added recipe from the recipe manager
        added_recipe = self.recipe_manager.data[3]

        # Check that the added recipe has the correct values
        self.assertEqual(added_recipe.id, 3)
        self.assertEqual(added_recipe.recipe_name, "New Recipe")
        self.assertEqual(added_recipe.recipe_author, "John")
        self.assertEqual(added_recipe.prep_time, 30)
        self.assertEqual(added_recipe.cook_time, 45)
        self.assertEqual(added_recipe.serving_size, 2)
        self.assertEqual(added_recipe.ingredients, [
            {"ingredientName": "ingredient1", "quantity": 1, "measurement": "unit"},
            {"ingredientName": "ingredient2", "quantity": 2, "measurement": "units"}
        ])
        self.assertEqual(added_recipe.instructions, {"1": "Step 1", "2": "Step 2"})

        # Modify the added recipe
        modified_recipe = Recipe(
            3,
            "Modified Recipe",
            "Jane",
            60,
            90,
            4,
            [
                {"ingredientName": "ingredient3", "quantity": 3, "measurement": "cups"},
                {"ingredientName": "ingredient4", "quantity": 4, "measurement": "tbsp"}
            ],
            {"1": "Step 1", "2": "Step 2", "3": "Step 3"}
        )

        # Edit the recipe in the recipe manager
        self.recipe_manager.editRecipe(modified_recipe)

        # Retrieve the modified recipe from the recipe manager
        modified_recipe = self.recipe_manager.data[3]

        # Check that the modified recipe has the updated values
        self.assertEqual(modified_recipe.recipe_name, "Modified Recipe")
        self.assertEqual(modified_recipe.recipe_author, "Jane")
        self.assertEqual(modified_recipe.prep_time, 60)
        self.assertEqual(modified_recipe.cook_time, 90)
        self.assertEqual(modified_recipe.serving_size, 4)
        self.assertEqual(modified_recipe.ingredients, [
            {"ingredientName": "ingredient3", "quantity": 3, "measurement": "cups"},
            {"ingredientName": "ingredient4", "quantity": 4, "measurement": "tbsp"}
        ])
        self.assertEqual(modified_recipe.instructions, {"1": "Step 1", "2": "Step 2", "3": "Step 3"})

    def tearDown(self):
        self.recipe_manager = None


if __name__ == '__main__':
    unittest.main()
