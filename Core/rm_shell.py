import os
import sys

# Get the absolute path of the directory containing this script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Add the Core directory to the Python module search path
core_dir = os.path.join(script_dir, 'Core')
sys.path.append(core_dir)

# Change the import statement to use the absolute path
from recipeProject import RecipeManager, Recipe
import cmd
import re


def validate_windows_file_name(file_name):
    # Check if file name is empty
    if not file_name:
        return False

    # Check if file name exceeds the maximum length
    if len(file_name) > 255:
        return False

    # Check if file name contains reserved characters
    reserved_chars = r'<>:"/\|?*'
    if any(char in reserved_chars for char in file_name):
        return False

    # Check if file name ends with a space or period
    if file_name[-1] in [' ', '.']:
        return False

    # Check if file name is a reserved device name
    reserved_device_names = ['CON', 'PRN', 'AUX', 'NUL',
                             'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9',
                             'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9']
    if file_name.upper() in reserved_device_names:
        return False

    # Check if file name contains any invalid characters
    invalid_chars_regex = r'[<>:"/\\|?*\x00-\x1F\x7F]'
    if re.search(invalid_chars_regex, file_name):
        return False

    return True


rm = RecipeManager()

class RmMode(cmd.Cmd):
    intro = 'Welcome to Recipe Manager!'
    prompt = 'RmMode> '

    def do_view(self,arg):
        'Help text'
        pass

    def do_add(self,arg):
        '\nAdds a recipe to recipes list. \n\tCommand: add'

        if arg:
            print('Add command does not take any arguments.')
            return
        
        lst = ['Recipe Name', 'Recipe Author', 'Preperation time','Cook time','Serving Size', 'Ingredients','Instructions']
        dic = {'Ingredients':[],'Recipe Name':None, 'Recipe Author':None, 'Preperation time':None,'Cook time':None,'Serving Size':None, 'Instructions':{}}
        for i in dic.keys():

            
            
            if i == "Ingredients":
                print('Enter ' + i + ' (enter "exit" to cancel operation.)')

                while True:
                    try:
                        num = input('\t>>> How many ingredients do you want to enter? ')
                        num = int(num)
                        if 0 < num < 20:
                            break
                        else:
                            print('Please enter an integer greater than 0 but less than 20.')
                    except ValueError:
                        print('Please enter a valid integer greater than 0 but less than 20.')
                    

                for j in range(int(num)):
                    
                    temp = {}
                    print('Entering Ingredient ' + str(j))

                    for k in ['ingredientName','quantity','measurement']:
                        user_input = input('\t>>> Enter ' + k + ': ')

                        if user_input == "exit":
                            print('\t>>>Nothing was added to the Recipe Manager.')
                            print(dic)
                            return

                        temp[k] = user_input
                    dic[i].append(temp) 


            elif i == "Instructions":
                pass

            else:
                print('Enter ' + i + ' (enter "exit" to cancel adding recipes)')
                user_input = input('\t>>> ')

                if user_input == "exit":
                    print('Nothing was added to the Recipe Manager.')
                    print(dic)
                    return

                dic[i] = user_input

        print(dic)

    def do_edit(self,arg):
        'Help text'
        pass

    def do_delete(self,arg):
        'Help text'
        pass

    def do_export(self, arg):
        '\nExport current recipe data in memory to a JSON file in Core/exports directory.If no filename argument is supplied, the JSON file will be exported with the default name.\n\tCommand: export <filename>.\n '
        arg = str(arg)
        if arg:
            if '.' in arg:
                if arg[-(len(arg)-arg.index('.')):] == '.json':
                    arg = arg[:-5]
                    
            
            if validate_windows_file_name(arg):
                rm.exportRecipes(arg)
            else:
                print(f"Invalid file name: {arg}. Please provide a valid Windows file name.")

        else:
            rm.exportRecipes()

    def do_import(self,arg):
        'Import a JSON file containing recipe data for Recipe Manager. Command: import <filename>'
        if arg:                            
            if arg[-5:] == '.json':
                arg = arg[:-5]

            rm.importRecipes(arg)

    def do_exit(self,arg):
        'Exits RmMode shell. \n\tCommand: exit\n'
        print('Thank you for using Recipe Manager!')

        return True


if __name__ == '__main__':
    RmMode().cmdloop()