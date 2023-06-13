import unittest
from Core.recipeProject import RecipeManager, Recipe
import sys
from io import StringIO

class TestRecipeManagerIntegration(unittest.TestCase):

    def test_CRUD(self):
        rm = RecipeManager()

        #Add new recipe
        newRecipe = Recipe(
            3,
            "Banana Milkshake",
            "Samuel",
            5,
            1,
            2,
            [
                {"ingredientName": "ice cube", "quantity": 3, "measurement": "unit"},
                {"ingredientName": "milk", "quantity": 1, "measurement": "cup"},
                {"ingredientName": "banana", "quantity": 1, "measurement": "unit"},
                {"ingredientName": "white sugar", "quantity": 1, "measurement": "tbsp"},
                {"ingredientName": "ground cinnamon", "quantity": 1, "measurement": "pinch"}
            ],
            {
                "1": "Gather all ingredients.",
                "2": "Combine ice, milk, banana, sugar, and cinnamon in a blender; blend until smooth."
            }
        )

        rm.addRecipe(newRecipe)
        # Test adding the new recipe
        self.assertIn(newRecipe, rm.data)

        # Test viewing the recipe
        captured_output = StringIO()
        sys.stdout = captured_output

        rm.viewRecipeList()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()

        expected = """ID  RecipeName              RecipeAuthor PrepTime  CookTime  ServingSize
---------------------------------------------------------------------
0   McBurger                Sam          10        12        1
1   Spaghetti Bolognese     Fehd         15        30        4
2   Chocolate Chip Cooki    Salmoan      20        15        24
3   Banana Milkshake        Samuel       5         1         2
"""

        self.assertEqual(output,expected)

        #Updating the added recipe
        modified_recipe = Recipe(
            3,
            "Mango Milkshake",
            "Samsun",
            7,
            2,
            3,
            [
                {"ingredientName": "ice cube", "quantity": 4, "measurement": "unit"},
                {"ingredientName": "milk", "quantity": 1, "measurement": "cup"},
                {"ingredientName": "mango", "quantity": 2, "measurement": "unit"},
                {"ingredientName": "white sugar", "quantity": 1, "measurement": "tbsp"}
            ],
            {
                "1": "Gather all ingredients.",
                "2": "Combine ice, milk, mango, and sugar in a blender; blend until smooth."
            }
        )

        rm.editRecipe(modified_recipe)

        #Test updating the recipe
        edited_recipe = rm.data[3]
        self.assertEqual(edited_recipe.id, 3)
        self.assertEqual(edited_recipe.recipe_name, "Mango Milkshake")
        self.assertEqual(edited_recipe.recipe_author, "Samsun")
        self.assertEqual(edited_recipe.prep_time, 7)
        self.assertEqual(edited_recipe.cook_time, 2)
        self.assertEqual(edited_recipe.serving_size, 3)
        self.assertEqual(edited_recipe.ingredients, [
            {"ingredientName": "ice cube", "quantity": 4, "measurement": "unit"},
            {"ingredientName": "milk", "quantity": 1, "measurement": "cup"},
            {"ingredientName": "mango", "quantity": 2, "measurement": "unit"},
            {"ingredientName": "white sugar", "quantity": 1, "measurement": "tbsp"}
        ])
        self.assertEqual(edited_recipe.instructions, {"1": "Gather all ingredients.", "2": "Combine ice, milk, mango, and sugar in a blender; blend until smooth."})
        
        #Delete the recipe
        rm.deleteRecipe(3)
        itemZero = next((recipe for recipe in rm.data if recipe.id == 3), None)

        #Test deleting the recipe
        self.assertEqual(None, itemZero)
        

