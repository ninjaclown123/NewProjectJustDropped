import unittest

import unittest
from Core.recipeProject import RecipeManager, Recipe


class TestRecipeManagerIntegration(unittest.TestCase):


    def test_addRecipe_and_viewRecipe(self):
        rm = RecipeManager()
        new_recipe = Recipe(
            3,
            "twester",
            "Raid",
            40,
            50,
            2,
            [
                {"ingredientName": "spicy fries", "quantity": 3, "measurement": "pieces"},
                {"ingredientName": "pepsi", "quantity": 1, "measurement": "cup"},
                {"ingredientName": "sos", "quantity": 1, "measurement": "sosCup"},
            ],
            {
                "1": "Add the sos.",
                "2": "Add the spicy fries with pepsi.",
            }
        )

        rm.addRecipe(new_recipe)
        recipe_list = rm.viewRecipeList()

        self.assertNotIn(new_recipe, recipe_list)
        self.assertEqual(len(recipe_list),1)
        self.assertEqual(recipe_list[0].id, 3)
        self.assertEqual(recipe_list[0].recipeName, "twester")
        self.assertEqual(recipe_list[0].recipeAuthor, "Raid")
        self.assertEqual(recipe_list[0].prepTime, 40)
        self.assertEqual(recipe_list[0].cookTime, 50)
        self.assertEqual(recipe_list[0].servingSize, 2)
        self.assertEqual(recipe_list[0].ingredients, [

            {"ingredientName": "spicy fries", "quantity": 3, "measurement": "pieces"},
            {"ingredientName": "pepsi", "quantity": 1, "measurement": "cup"},
            {"ingredientName": "sos", "quantity": 1, "measurement": "sosCup"},
        ])
        
        self.assertEqual(recipe_list[0].istructions, {
            "1":  "Add the sos.",
            "2": "Add the spicy fries"
        })

        self.assertIn(new_recipe, rm.data)


if __name__ == "__main__":
    unittest.main()


        


