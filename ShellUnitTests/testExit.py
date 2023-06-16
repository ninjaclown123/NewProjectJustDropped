import os
import sys
import unittest

# Get the absolute path of the directory containing this script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Add the Core directory to the Python module search path
core_dir = os.path.join(script_dir, '..', 'Core')
sys.path.append(core_dir)

# Import the module you want to test
from Core.rm_shell import RmMode
from unittest.mock import patch

class YourCmdTestCase(unittest.TestCase):
    def setUp(self):
        # Initialize an instance of YourCmdClass for testing
        self.RmMode = RmMode()
        

    @patch('builtins.print')
    def test_exit(self, mock_print):
        result = self.RmMode.do_exit('')

        self.assertTrue(result)

        mock_print.assert_called_with('Thank you for using Recipe Manager!')

        
