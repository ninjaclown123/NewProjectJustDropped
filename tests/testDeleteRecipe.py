import unittest
from Core.recipeProject import RecipeManager

class TestRecipeManagement(unittest.TestCase):

    # tests basic functionality
    # expected: the system will delete the item with the specified id.
    def test_delete_recipe(self):
        rm = RecipeManager()
        rm.deleteRecipe(0)
        itemZero = next((recipe for recipe in rm.data if recipe.id == 0), None)
        self.assertEqual(None, itemZero)

    # tests deleting non-existent id
    # expected: the method will not delete the non-existent item.
    def test_delete_recipe_NON_EXISTENT_ID(self):
        rm = RecipeManager()
        count = len(rm.data)
        rm.deleteRecipe(846)
        self.assertEqual(count, len(rm.data))

    # tests deleting string id
    # expected: the method will not delete the recipe.
    def test_delete_recipe_STRING_ID(self):
        rm = RecipeManager()
        rm.deleteRecipe("0")
        itemZero = next((recipe for recipe in rm.data if recipe.id == 0), None)
        self.assertIn(itemZero, rm.data)

if __name__ == '__main__':
    unittest.main()