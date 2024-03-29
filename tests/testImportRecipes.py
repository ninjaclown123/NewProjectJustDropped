import unittest


from Core.recipeProject import RecipeManager, Recipe

class TestRecipeManagement(unittest.TestCase):

    def test_import_NoFile(self):
        rm = RecipeManager()

        rm.data = []

        result = rm.importRecipes('Bruh.jsonnnnnnnn')

        self.assertEqual(result,"File404")


    def test_import_recipes(self):
        rm = RecipeManager()

        rm.data = []

        recipe1 = Recipe(
            0,
            "McBurger",
            "Sam",
            10,
            12,
            1,
            [
                {"ingredientName": "bun", "quantity": 1, "measurement": "unit"},
                {"ingredientName": "secretPatty",
                    "quantity": 1, "measurement": "unit"},
                {"ingredientName": "specialMayo",
                    "quantity": 10, "measurement": "grams"},
                {"ingredientName": "specialSauce",
                    "quantity": 20, "measurement": "grams"},
                {"ingredientName": "lettuce", "quantity": 8, "measurement": "grams"},
                {"ingredientName": "tomato", "quantity": 8, "measurement": "grams"}
            ],
            {
                "1": "Assemble the bun and the secret patty.",
                "2": "Spread special mayo and special sauce on the bun.",
                "3": "Add lettuce and tomato on top.",
                "4": "Cook the assembled burger for 12 minutes."
            }
        )
        recipe2 = Recipe(
            1,
            "Spaghetti Bolognese",
            "Fehd",
            15,
            30,
            4,
            [
                {"ingredientName": "spaghetti",
                 "quantity": 250, "measurement": "grams"},
                {"ingredientName": "ground beef",
                 "quantity": 500, "measurement": "grams"},
                {"ingredientName": "onion", "quantity": 1,
                 "measurement": "units"},
                {"ingredientName": "garlic",
                 "quantity": 2, "measurement": "grams"},
                {"ingredientName": "tomato sauce",
                 "quantity": 400, "measurement": "grams"},
                {"ingredientName": "tomato paste",
                 "quantity": 2, "measurement": "tablespoons"},
                {"ingredientName": "olive oil", "quantity": 2,
                 "measurement": "tablespoons"},
                {"ingredientName": "dried oregano",
                 "quantity": 1, "measurement": "teaspoon"},
                {"ingredientName": "salt", "quantity": 1,
                 "measurement": "teaspoon"},
                {"ingredientName": "black pepper",
                 "quantity": 1, "measurement": "teaspoon"}
            ],
            {
                "1": "Cook spaghetti according to package instructions.",
                "2": "In a separate pan, heat olive oil and sauté onion and garlic until translucent.",
                "3": "Add ground beef and cook until browned.",
                "4": "Stir in tomato sauce and tomato paste. Simmer for 10 minutes.",
                "5": "Season with dried oregano, salt, and black pepper.",
                "6": "Serve the Bolognese sauce over cooked spaghetti."
            }
        )
        recipe3 = Recipe(
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

        data = [recipe1, recipe2, recipe3]


        rm.importRecipes('unittestRecipeImport')
        print(data)
        for i in range(len(data)):
            self.assertEqual(data[i].id,rm.data[i].id)
            self.assertEqual(data[i].recipe_name,rm.data[i].recipe_name)
            self.assertEqual(data[i].recipe_author,rm.data[i].recipe_author)
            self.assertEqual(data[i].ingredients,rm.data[i].ingredients)