import os
import sys
import unittest

# Get the absolute path of the directory containing this script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Add the Core directory to the Python module search path
core_dir = os.path.join(script_dir, '..', 'Core')
sys.path.append(core_dir)

# Import the module you want to test
from Core.rm_shell import RmMode, RecipeManager
from unittest.mock import patch, MagicMock


from unittest.mock import patch
from io import StringIO

class RecipeManagerTestCase(unittest.TestCase):

    def setUp(self):
        self.rm_mode = RmMode()

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input')
    def test_do_add(self, mock_input, mock_stdout):
        # Set up the mock input values
        mock_input.side_effect = [
            "Generic Burger",    # Recipe Name
            "Generic Author",    # Recipe Author
            "9",                 # Preparation time
            "2",                 # Cook time
            "2",                 # Serving Size
            "3",                 # Number of ingredients
            "Generic Buns",      # Ingredient 1: ingredientName
            "unit",              # Ingredient 1: measurement
            "1",                 # Ingredient 1: quantity
            "Generic Ham",       # Ingredient 2: ingredientName
            "grams",             # Ingredient 2: measurement
            "25",                # Ingredient 2: quantity
            "lettuce",           # Ingredient 3: ingredientName
            "grams",             # Ingredient 3: measurement
            "10",                # Ingredient 3: quantity
            "3",                 # Number of instructions
            "Take generic buns",       # Instruction 1
            "Take generic patty",      # Instruction 2
            "Assemble with lettuce",   # Instruction 3
            "y"                  # Add recipe to Recipe Manager
        ]

        # Mock the RecipeManager instance
        self.rm_mode.rm = MagicMock()

        # Call the do_add method
        self.rm_mode.do_add(None)

        # Get the captured output
        output = mock_stdout.getvalue()
        # self.assertEqual(self.rm_mode.rm.data[1].id,99)
        # Verify the output
        self.assertIn("Generic Burger by Generic Author added to Recipe Manager.", output)

if __name__ == "__main__":
    unittest.main()