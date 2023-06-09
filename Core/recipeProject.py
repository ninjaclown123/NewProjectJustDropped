import json
import os


class Recipe:
    def __init__(self, recipe_name, recipe_author, prep_time, cook_time, serving_size, ingredients, instructions):
        self.recipe_name = recipe_name
        self.recipe_author = recipe_author
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.serving_size = serving_size
        self.ingredients = ingredients
        self.instructions = instructions

    def __str__(self):
        ingredient_list = "\n".join(
            [f"{ing['ingredientName']}: {ing['quantity']} {ing['measurement']}" for ing in self.ingredients])
        instructions_list = "\n".join(
            [f"{step}. {self.instructions[step]}" for step in self.instructions])
        return f"Recipe: {self.recipe_name}\nAuthor: {self.recipe_author}\nPreparation Time: {self.prep_time} minutes\nCook Time: {self.cook_time} minutes\nServing Size: {self.serving_size}\nIngredients:\n{ingredient_list}\nInstructions:\n{instructions_list}"


class RecipeManager:
    def __init__(self):
        self.data = [
            {
                "id": 0,
                "recipeName": "McBurger",
                "recipeAuthor": "Sam",
                "prepTime": 10,
                "cookTime": 12,
                "servingSize": 1,
                "ingredients": [
                    {"ingredientName": "bun", "quantity": 1, "measurement": "unit"},
                    {"ingredientName": "secretPatty",
                     "quantity": 1, "measurement": "unit"},
                    {"ingredientName": "specialMayo",
                     "quantity": 10, "measurement": "grams"},
                    {"ingredientName": "specialSauce",
                     "quantity": 20, "measurement": "grams"},
                    {"ingredientName": "lettuce",
                     "quantity": 8, "measurement": "grams"},
                    {"ingredientName": "tomato",
                     "quantity": 8, "measurement": "grams"}
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

    def viewRecipe(self):  # raid
        # this method should print all recipes to the screen.
        recpice_manager = RecipeManager()
        recipe = recpice_manager.data[0]
        recpie_obj = Recipe(
            recipe['recipeName'],
            recipe['recpeAuthor'],
            recipe['prepTime'],
            recipe['cookTime'],
            recipe['servingSize'],
            recipe['ingredients'],
            recipe['instructions']

        )
        recipe_str = str(recpie_obj)
        print(recipe_str)
        pass

    def addRecipe(self):  # fehad
        # this method should add a new recipe to the recipes list
        pass

    def editRecipe(self, id):  # hamza
        # this method should find a recipe by name and edit the recipe.
        pass

    def deleteRecipe(self, id):  # josh
        # this method should find a recipe by name and delete it.
        pass

    def exportRecipes(self, filename="DefaultExportName"):  # sam
        # exports recipes to a .json file

        if not os.path.exists("Core/exports/"):
            os.makedirs("Core/exports/")


        print(filename,'xxxx')
        filepath = "Core/exports/" + str(filename) + ".json"
        file = open(filepath, "w")

        json.dump(self.data, file, indent=4)

        file.close()

        print("export success")

        return True

    def importRecipes(self):  # sam
        # imports recipes from a .json file
        pass


recipe = Recipe(
    "McBurger",
    "Sam",
    10,
    12,
    1,
    [
        {"ingredientName": "bun", "quantity": 1, "measurement": "unit"},
        {"ingredientName": "secretPatty", "quantity": 1, "measurement": "unit"},
        {"ingredientName": "specialMayo", "quantity": 10, "measurement": "gram"},
        {"ingredientName": "specialSauce", "quantity": 20, "measurement": "gram"},
        {"ingredientName": "lettuce", "quantity": 8, "measurement": "gram"},
        {"ingredientName": "tomato", "quantity": 8, "measurement": "gram"}
    ],
    {
        1: "Assemble the bun and the secret patty.",
        2: "Spread special mayo and special sauce on the bun.",
        3: "Add lettuce and tomato on top.",
        4: "Cook the assembled burger for 12 minutes."
    }
)


# rm = RecipeManager()

# rm.exportRecipes("testingRecipe23")


