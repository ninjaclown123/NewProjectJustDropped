import unittest
from Core.recipeProject import RecipeManager, Recipe


class TestRecipeManagement(unittest.TestCase):

    def setUp(self):
        # Create a RecipeManager instance for testing
        self.recipe_manager = RecipeManager()

    def test_editRecipe_existingRecipe(self):
        # Create a new recipe to be used for editing
        new_recipe = Recipe(
            1,
            "Updated Recipe",
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

        # Edit an existing recipe in the RecipeManager's data
        self.recipe_manager.data = [
            Recipe(0, "Recipe 1", "Author 1", 10, 20, 3, [], {}),
            Recipe(1, "Recipe 2", "Author 2", 15, 25, 4, [], {})
        ]
        self.recipe_manager.editRecipe(new_recipe)

        # Check if the recipe was edited correctly
        edited_recipe = self.recipe_manager.data[1]
        self.assertEqual(edited_recipe.id, 1)
        self.assertEqual(edited_recipe.recipe_name, "Updated Recipe")
        self.assertEqual(edited_recipe.recipe_author, "John")
        self.assertEqual(edited_recipe.prep_time, 30)
        self.assertEqual(edited_recipe.cook_time, 45)
        self.assertEqual(edited_recipe.serving_size, 2)
        self.assertEqual(edited_recipe.ingredients, [
            {"ingredientName": "ingredient1", "quantity": 1, "measurement": "unit"},
            {"ingredientName": "ingredient2", "quantity": 2, "measurement": "units"}
        ])
        self.assertEqual(edited_recipe.instructions, {"1": "Step 1", "2": "Step 2"})

    def test_editRecipe_nonExistingRecipe(self):
        # Create a new recipe to be used for editing
        new_recipe = Recipe(
            3,
            "New Recipe",
            "Jane",
            20,
            30,
            1,
            [
                {"ingredientName": "ingredient1", "quantity": 1, "measurement": "unit"}
            ],
            {"1": "Step 1"}
        )

        # Edit a non-existing recipe in the RecipeManager's data
        self.recipe_manager.data = [
            Recipe(0, "Recipe 1", "Author 1", 10, 20, 3, [], {}),
            Recipe(1, "Recipe 2", "Author 2", 15, 25, 4, [], {})
        ]

        # Use assertRaises to check if ValueError is raised
        with self.assertRaises(ValueError):
            self.recipe_manager.editRecipe(new_recipe)

        # Check that the data remains unchanged
        self.assertEqual(len(self.recipe_manager.data), 2)

    def test_editRecipe_noChanges(self):
        # Create a new recipe to be used for editing
        new_recipe = Recipe(
            1,
            "Recipe 1",
            "Author 1",
            10,
            20,
            2,
            [],
            {}
        )

        # Add the recipe to the data
        self.recipe_manager.data = [
            new_recipe,
            Recipe(1, "Recipe 2", "Author 2", 15, 25, 4, [], {})
        ]

        self.recipe_manager.editRecipe(new_recipe)

        # Check that the data remains unchanged
        self.assertEqual(len(self.recipe_manager.data), 2)
        self.assertEqual(self.recipe_manager.data[0], new_recipe)

    def test_editRecipe_emptyData(self):
        # Create a new recipe to be used for editing
        new_recipe = Recipe(
            1,
            "Updated Recipe",
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

        # Edit a recipe when the data is empty
        self.recipe_manager.data = []

        # Use assertRaises to check if ValueError is raised
        with self.assertRaises(ValueError):
            self.recipe_manager.editRecipe(new_recipe)

        # Check that the data remains empty
        self.assertEqual(len(self.recipe_manager.data), 0)


if __name__ == '__main__':
    unittest.main()
