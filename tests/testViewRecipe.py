import unittest

from Core.recipeProject import RecipeManager, Recipe


class TestRecipeManagement(unittest.TestCase):
    def viewRecipeList(self):
        self.recipe_manager = RecipeManager()
        self.recipes = []
        for recipe_data in self.recipe_manager.data:
            recipe_obj = Recipe(
                recipe_data['recipeName'],
                recipe_data['recipeAuthor'],
                recipe_data['prepTime'],
                recipe_data['cookTime'],
                recipe_data['servingSize'],
                recipe_data['ingredients'],
                recipe_data['instructions']
            )
            self.recipes.append(recipe_obj)

    def test_view_recipes_List(self):
        rm = RecipeManager()
        
        testData = [
            {
                "id": 0,
                "recipeName": "McBurger",
                "recipeAuthor": "Sam",
                "prepTime": 10,
                "cookTime": 12,
                "servingSize": 1,
                "ingredients": [
                    {"ingredientName": "bun", "quantity": 1, "measurement": "unit"},
                    {"ingredientName": "secretPatty", "quantity": 1, "measurement": "unit"},
                    {"ingredientName": "specialMayo", "quantity": 10, "measurement": "grams"},
                    {"ingredientName": "specialSauce", "quantity": 20, "measurement": "grams"},
                    {"ingredientName": "lettuce", "quantity": 8, "measurement": "grams"},
                    {"ingredientName": "tomato", "quantity": 8, "measurement": "grams"}
                ],
                "instructions": {
                    "1": "Assemble the bun and the secret patty.",
                    "2": "Spread special mayo and special sauce on the bun.",
                    "3": "Add lettuce and tomato on top.",
                    "4": "Cook the assembled burger for 12 minutes."
                }
            },
            {
                "id": 1,
                "recipeName": "Spaghetti Bolognese",
                "recipeAuthor": "Fahed",
                "prepTime": 15,
                "cookTime": 30,
                "servingSize": 4,
                "ingredients": [
                    {"ingredientName": "spaghetti", "quantity": 250, "measurement": "grams"},
                    {"ingredientName": "ground beef", "quantity": 500, "measurement": "grams"},
                    {"ingredientName": "onion", "quantity": 1, "measurement": "units"},
                    {"ingredientName": "garlic", "quantity": 2, "measurement": "grams"},
                    {"ingredientName": "tomato sauce", "quantity": 400, "measurement": "grams"},
                    {"ingredientName": "tomato paste", "quantity": 2, "measurement": "tablespoons"},
                    {"ingredientName": "olive oil", "quantity": 2, "measurement": "tablespoons"},
                    {"ingredientName": "dried oregano", "quantity": 1, "measurement": "teaspoon"},
                    {"ingredientName": "salt", "quantity": 1, "measurement": "teaspoon"},
                    {"ingredientName": "black pepper", "quantity": 1, "measurement": "teaspoon"}
                ],
                "instructions": {
                    "1": "Cook spaghetti according to package instructions.",
                    "2": "In a separate pan, heat olive oil and sauté onion and garlic until translucent.",
                    "3": "Add ground beef and cook until browned.",
                    "4": "Stir in tomato sauce and tomato paste. Simmer for 10 minutes.",
                    "5": "Season with dried oregano, salt, and black pepper.",
                    "6": "Serve the Bolognese sauce over cooked spaghetti."
                }
            },
            {
                "id": 2,
                "recipeName": "Chocolate Chip Cookies",
                "recipeAuthor": "Salmoan",
                "prepTime": 20,
                "cookTime": 15,
                "servingSize": 24,
                "ingredients": [
                    {"ingredientName": "all-purpose flour", "quantity": 2.5, "measurement": "cups"},
                    {"ingredientName": "butter", "quantity": 1, "measurement": "cups"},
                    {"ingredientName": "granulated sugar", "quantity": 1, "measurement": "cups"},
                    {"ingredientName": "brown sugar", "quantity": 1, "measurement": "cups"},
                    {"ingredientName": "eggs", "quantity": 2, "measurement": "units"},
                    {"ingredientName": "vanilla extract", "quantity": 2, "measurement": "teaspoons"},
                    {"ingredientName": "baking soda", "quantity": 1, "measurement": "teaspoon"},
                    {"ingredientName": "salt", "quantity": 1, "measurement": "teaspoon"},
                    {"ingredientName": "chocolate chips", "quantity": 2, "measurement": "cups"}
                ],
                "instructions": {
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
            }
        ]

        rm.data = testData
        


        expected_recipe_strings = [
            "Recipe: McBurger\nAuthor: Sam\nPreparation Time: 10 minutes\nCook Time: 12 minutes\nServing Size: 1\nIngredients:\nbun: 1 unit\nsecretPatty: 1 unit\nspecialMayo: 10 grams\nspecialSauce: 20 grams\nlettuce: 8 grams\ntomato: 8 grams\nInstructions:\n1. Assemble the bun and the secret patty.\n2. Spread special mayo and special sauce on the bun.\n3. Add lettuce and tomato on top.\n4. Cook the assembled burger for 12 minutes.",
            "Recipe: Spaghetti Bolognese\nAuthor: Fahed\nPreparation Time: 15 minutes\nCook Time: 30 minutes\nServing Size: 4\nIngredients:\nspaghetti: 250 grams\nground beef: 500 grams\nonion: 1 units\ngarlic: 2 grams\ntomato sauce: 400 grams\ntomato paste: 2 tablespoons\nolive oil: 2 tablespoons\ndried oregano: 1 teaspoon\nsalt: 1 teaspoon\nblack pepper: 1 teaspoon\nInstructions:\n1. Cook spaghetti according to package instructions.\n2. In a separate pan, heat olive oil and sauté onion and garlic until translucent.\n3. Add ground beef and cook until browned.\n4. Stir in tomato sauce and tomato paste. Simmer for 10 minutes.\n5. Season with dried oregano, salt, and black pepper.\n6. Serve the Bolognese sauce over cooked spaghetti.",
            "Recipe: Chocolate Chip Cookies\nAuthor: Salmoan\nPreparation Time: 20 minutes\nCook Time: 15 minutes\nServing Size: 24\nIngredients:\nall-purpose flour: 2.5 cups\nbutter: 1 cups\ngranulated sugar: 1 cups\nbrown sugar: 1 cups\neggs: 2 units\nvanilla extract: 2 teaspoons\nbaking soda: 1 teaspoon\nsalt: 1 teaspoon\nchocolate chips: 2 cups\nInstructions:\n1. Preheat oven to 375°F (190°C).\n2. In a large bowl, cream together butter, granulated sugar, and brown sugar until smooth.\n3. Beat in eggs one at a time, then stir in vanilla extract.\n4. In a separate bowl, combine all-purpose flour, baking soda, and salt.\n5. Gradually add the dry ingredients to the butter mixture and mix well.\n6. Fold in the chocolate chips.\n7. Drop rounded tablespoons of dough onto ungreased baking sheets.\n8. Bake for 10-12 minutes until edges are lightly golden.\n9. Allow cookies to cool on baking sheets for a few minutes before transferring to wire racks to cool completely."
        ]

        for i, recipe in enumerate(self.recipes):
            recipe_str = str(recipe)
            expected_str = expected_recipe_strings[i]
            self.assertEqual(recipe_str, expected_str)

if __name__ == '__main__':
    unittest.main()
