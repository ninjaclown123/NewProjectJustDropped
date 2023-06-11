import sys
from io import StringIO
import unittest
from Core.recipeProject import RecipeManager

class TestRecipeManagement(unittest.TestCase):

    def test_view_recipe(self):
        rm = RecipeManager()

        captured_output = StringIO()
        sys.stdout = captured_output

        rm.viewRecipeList()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        print('line19')
        expected = """ID  RecipeName              RecipeAuthor PrepTime  CookTime  ServingSize
---------------------------------------------------------------------
0   McBurger                Sam          10        12        1
1   Spaghetti Bolognese     Fehd         15        30        4
2   Chocolate Chip Cooki    Salmoan      20        15        24
"""

        self.assertEqual(output,expected)