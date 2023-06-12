import unittest
from Core.recipeProject import RecipeManager

class TestRecipeManagerIntegration(unittest.TestCase):

    def test_CRUD(self):
        rm = RecipeManager()

        newRecipe = {
            "id": 3,
            "recipeName": "Banana Milkshake",
            "recipeAuthor": "Samuel",
            "prepTime": 5,
            "cookTime": 1,
            "servingSize": 2,
            "ingredients": [
                {"ingredientName": "ice cube", "quantity": 3, "measurement": "unit"},
                {"ingredientName": "milk", "quantity": 1, "measurement": "cup"},
                {"ingredientName": "banana", "quantity": 1, "measurement": "unit"},
                {"ingredientName": "white sugar", "quantity": 1, "measurement": "tbsp"},
                {"ingredientName": "ground cinnamon", "quantity": 1, "measurement": "pinch"},

            ],
            "instructions": {
                "1": "Gather all ingredients.",
                "2": "Combine ice, milk, banana, sugar, and cinnamon in a blender; blend until smooth.",
            }
        }

        # Test adding the new recipe
        rm.addRecipe(newRecipe)
        self.assertIn(newRecipe, rm.data)

        # Test viewing the recipe


        # Test updating the recipe
        updated = rm.updateRecipe(3, new_recipe_name="Mango Milkshake", new_recipe_author="Samson",
                                  new_prep_time=5, new_cook_time=1, new_serving_size=2)
        self.assertTrue(updated)
        self.assertEqual(rm.data[-1]['recipeName'], "Mango Milkshake")
        self.assertEqual(rm.data[-1]['recipeAuthor'], "Samson")
        self.assertEqual(rm.data[-1]['prepTime'], 5)
        self.assertEqual(rm.data[-1]['cookTime'], 1)
        self.assertEqual(rm.data[-1]['servingSize'], 2)

        #Test deleting the recipe
        rm.deleteRecipe(3)
        delete = next((recipe for recipe in rm.data if recipe.get("id") == 3), None)
        self.assertEqual(None, delete)

