import unittest
from Core.recipeProject import RecipeManager, Recipe

class TestRecipeManagement(unittest.TestCase):

    def test_add_recipe(self):
        rm = RecipeManager()

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
        self.assertIn(newRecipe, rm.data)
    
    def test_add_recipe_wrongID(self):
        rm = RecipeManager()

        newRecipe = Recipe(
            2,
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

        with self.assertRaises(Exception):
            rm.addRecipe(newRecipe)
    
    def test_add_recipe_wrongName(self):
        rm = RecipeManager()
       
        newRecipe = Recipe(
            2,
            "Chocolate Chip Cookies",
            "Salmoan",
            20,
            15,
            24,
            [
                {"ingredientName": "all-purpose flour",
                 "quantity": 2.5, "measurement": "cups"},
                {"ingredientName": "butter",
                 "quantity": 1, "measurement": "cups"},
                {"ingredientName": "granulated sugar",
                 "quantity": 1, "measurement": "cups"},
                {"ingredientName": "brown sugar",
                 "quantity": 1, "measurement": "cups"},
                {"ingredientName": "eggs", "quantity": 2,
                 "measurement": "units"},
                {"ingredientName": "vanilla extract",
                 "quantity": 2, "measurement": "teaspoons"},
                {"ingredientName": "baking soda",
                 "quantity": 1, "measurement": "teaspoon"},
                {"ingredientName": "salt", "quantity": 1,
                 "measurement": "teaspoon"},
                {"ingredientName": "chocolate chips",
                 "quantity": 2, "measurement": "cups"}
            ],
            {
                "1": "Preheat oven to 375°F (190°C).",
                "2": "In a large bowl, cream together butter, granulated sugar, and brown sugar until smooth.",
                "3": "Beat in eggs one at a time, then stir in vanilla extract.",
                "4": "In a separate bowl, combine all-purpose flour, baking soda, and salt.",
                "5": "Gradually add the dry ingredients to the butter mixture and mix well.",
                "6": "Fold in the chocolate chips.",
                "7": "Drop rounded tablespoons of dough onto ungreased baking sheets.",
                "8": "Bake for 10-12 minutes until edges are lightly golden.",
                "9": "Allow cookies to cool on baking sheets for a few minutes before transferring to wire racks to cool completely."
            }
        )

        with self.assertRaises(Exception):
            rm.addRecipe(newRecipe)
    