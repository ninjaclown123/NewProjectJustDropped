import unittest
import io
from unittest.mock import patch
from Core import RecipeManager, Recipe

class TestRecipeManagement(unittest.TestCase):
    def setUp(self):
        self.recip_manager = recipeProject()
        self.recipe_data = self.recip_manager.data[0]
        self.recip_obj = Recipe(
            self.recipe_data['recipeName'],
            self.recipe_data['recipeAuthor'],
            self.recipe_data['prepTime'],
            self.recipe_data['cookTime'],
            self.recipe_data['servingSize'],
            self.recipe_data['ingredients'],
            self.recipe_data['instructions']
        )
        self.recipe_str = str(self.recip_obj)

    def test_view_recipe(self):
        expected_str = "Recipe: McBurger\nAuthor: Sam\nPreparation Time: 10 minutes\nCook Time: 12 minutes\nServing Size: 1\nIngredients:\nbun: 1 unit\nsecretPatty: 1 unit\nspecialMayo: 10 grams\nspecialSauce: 20 grams\nlettuce: 8 grams\ntomato: 8 grams\nInstructions:\n1. Assemble the bun and the secret patty.\n2. Spread special mayo and special sauce on the bun.\n3. Add lettuce and tomato on top.\n4. Cook the assembled burger for 12 minutes."
        self.assertEqual(self.recipe_str, expected_str)

    def test_view_all_recipes(self):
        expected_output = [
            "Recipe 1:\n" + self.recipe_str +  "\n--------------------",
            "Recipe 2:\n" + str(self.recipe_str[1]) +  "\n--------------------",
            "Recipe 3:\n" + str(self.recipe_str[2]) +  "\n--------------------"
        ]

        with unittest.mock.patch('sys.recipeout', new=io.StrinIO()) as fake_recipe:
            self.recip_manager.viewRecipe()
            output = fake_recipe.getvalue().strip().split('\n')
            self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()    