import json
import os
from json.decoder import JSONDecodeError


class Recipe:

    def __init__(self, recipe_id, recipe_name, recipe_author, prep_time, cook_time, serving_size, ingredients, instructions):
        self.id = recipe_id
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
        # initial recipes for development purposes
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

        self.data = [recipe1, recipe2, recipe3]

    def viewRecipeList(self): #Raid
        print("{:<3} {:<23} {:<12} {:<9} {:<9} {}".format(
            "ID", "RecipeName", "RecipeAuthor", "PrepTime", "CookTime", "ServingSize"))
        print("---------------------------------------------------------------------")
        for recipe in self.data:
            if len(recipe.recipe_name) >= 20:
                rName = recipe.recipe_name[:-2]
                print("{:<3} {:<23} {:<12} {:<9} {:<9} {}".format(
                    recipe.id, rName, recipe.recipe_author, recipe.prep_time, recipe.cook_time, recipe.serving_size))
            else:
                print("{:<3} {:<23} {:<12} {:<9} {:<9} {}".format(
                    recipe.id, recipe.recipe_name, recipe.recipe_author, recipe.prep_time, recipe.cook_time, recipe.serving_size))

    def addRecipe(self, recipe):  # fahad
        # this method should add a new recipe to the recipes list
        for r in self.data:
            if r.id == recipe.id:
                raise Exception("Recipe with the same ID already exists!")
            if r.recipe_name == recipe.recipe_name:
                raise Exception("Recipe with the same name already exists!")
        self.data.append(recipe)

    def editRecipe(self, newRecipe):
        for recipe in self.data:
            if recipe.id == newRecipe.id:
                recipe.recipe_name = newRecipe.recipe_name or recipe.recipe_name
                recipe.recipe_author = newRecipe.recipe_author or recipe.recipe_author
                recipe.prep_time = newRecipe.prep_time or recipe.prep_time
                recipe.cook_time = newRecipe.cook_time or recipe.cook_time
                recipe.serving_size = newRecipe.serving_size or recipe.serving_size
                recipe.ingredients = newRecipe.ingredients or recipe.ingredients
                recipe.instructions = newRecipe.instructions or recipe.instructions
                return

        raise ValueError("Recipe ID not found in the list of recipes.")

    def deleteRecipe(self, id):  # josh
        for item in self.data:
            if item.id == id:
                self.data.remove(item)
                return

        print("ID not found in the list of recipes.")

    def exportRecipes(self, filename="DefaultExportName"):  # sam
        # exports recipes to a .json file

        mrJSON = []

        for i in self.data:
            mrJSON.append(
                {
                    "id": i.id,
                    "recipeName": i.recipe_name,
                    "recipeAuthor": i.recipe_author,
                    "prepTime": i.prep_time,
                    "cookTime": i.cook_time,
                    "servingSize": i.serving_size,
                    "ingredients": i.ingredients,
                    "instructions": i.instructions
                }
            )

        
        if not os.path.exists("Core/exports/"):
            os.makedirs("Core/exports/")

        filepath = "Core/exports/" + str(filename) + ".json"
        file = open(filepath, "w")

        json.dump(mrJSON, file, indent=4)

        file.close()

        print("Exported " + str(filename) + ' to ' +
              str(filepath) + ' Successfully.')

        return True

    def importRecipes(self, filename):  # sam
        # imports recipes from a .json file

        folder_path = 'Core/imports'

        if not os.path.exists(folder_path):
            print("Imports folder has not been initialized in Core/.")
            return "Import404"

        file_path = folder_path + '/' + str(filename) + '.json'

        if not os.path.exists(file_path):
            print('The file ' + str(filename) +
                  ' in ' + file_path + ' does not exist')
            return "File404"

        file = open(file_path, 'r')

        try:
            fileData = json.load(file)
            importData = []
            for i in fileData:
                recipe = Recipe(i["id"],i["recipeName"],i["recipeAuthor"],i["prepTime"],i["cookTime"],i["servingSize"],i["ingredients"],i["instructions"])
                importData.append(recipe)
            
            self.data = importData

            print('Imported ' + str(filename) + '.json from ' +
                  str(file_path) + ' successfully.')
            file.close()
            return True

        except JSONDecodeError:
            raise ValueError(
                f'The selected JSON file "{filename}.json" is corrupted.')


# rm = RecipeManager()

# # rm.data = []
# # recipe1 = Recipe(
# #             0,
# #             "McBurger",
# #             "Sam",
# #             10,
# #             12,
# #             1,
# #             [
# #                 {"ingredientName": "bun", "quantity": 1, "measurement": "unit"},
# #                 {"ingredientName": "secretPatty",
# #                     "quantity": 1, "measurement": "unit"},
# #                 {"ingredientName": "specialMayo",
# #                     "quantity": 10, "measurement": "grams"},
# #                 {"ingredientName": "specialSauce",
# #                     "quantity": 20, "measurement": "grams"},
# #                 {"ingredientName": "lettuce", "quantity": 8, "measurement": "grams"},
# #                 {"ingredientName": "tomato", "quantity": 8, "measurement": "grams"}
# #             ],
# #             {
# #                 "1": "Assemble the bun and the secret patty.",
# #                 "2": "Spread special mayo and special sauce on the bun.",
# #                 "3": "Add lettuce and tomato on top.",
# #                 "4": "Cook the assembled burger for 12 minutes."
# #             }
# #         )
# # # rm.addRecipe(recipe1)
# # # rm.addRecipe(recipe1)



# print(rm.data)

# rm.exportRecipes('objectTesting')

# rm.viewRecipeList()

# rm.updateRecipe(
#             id=0,
#             new_recipe_name="Vegan Bolognese",
#             new_recipe_author="Jane Doe",
#             new_prep_time=25,
#             new_cook_time=40,
#             new_serving_size=5
#         )

# rm.exportRecipes()
# rm.importRecipes('recipes')
# rm.exportRecipes('new')