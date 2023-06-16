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

def validate_quantity(quantity):
    try:
        quantity = int(quantity)
        if quantity > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def validate_ingredientname(ingredientName):
    if (
        len(ingredientName) <= 20
        and len(ingredientName) > 0
        and not ingredientName.isnumeric()
    ):
        return True
    else:
        return False
    
def validate_measurement(unit):
    if (
        len(unit) <= 20
        and len(unit) > 0
        and not unit.isnumeric()
    ):
        return True
    else:
        return False

rm = RecipeManager()

class RmMode(cmd.Cmd):
    intro = 'Welcome to Recipe Manager!'
    prompt = 'RmMode> '

    def do_view(self,arg):
        'Type in "view all" to view all the recipes OR type "view <id>" to view specific id!'
        arg = str(arg)
        check = True
        if arg:
            if arg.upper()=='ALL':
                rm.viewRecipeList()
            else:
                for i in arg:
                    if(i.isdigit()==False):
                        check = False
                        print("Please enter either 'ALL' to view all recipes OR a proper ID to view specific recipe!")
                        break
                if check==True:
                    try:
                        arg = int(arg)
                        rec = rm.viewSpecificRecipe(arg)
                        print(rec)
                    except Exception as err:
                        print(err)
                    
        else:
            print("Please enter a proper argument to process. You can type 'help view' for details.")

    def do_add(self,arg):
        '\nAdds a recipe to recipes list. \n\tCommand: add'

        if arg:
            print('Add command does not take any arguments.')
            return
        
        dic = {'Recipe Name':None, 'Recipe Author':None, 'Preparation time':None,'Cook time':None,'Serving Size':None,'Ingredients':[], 'Instructions':{}}

        print('You are now adding a recipe (enter "exit" to cancel operation)')
        for i in dic.keys():

            if i == "Ingredients":
                print('>>> Enter ' + i + ': ')

                while True:
                    try:
                        num = input('\t>>> How many ingredients do you want to enter? ')

                        if num == "exit":
                            print('\t>>> Nothing was added to the Recipe Manager.')
                            print(dic)
                            return

                        num = int(num)
                        if 0 < num < 20:
                            break
                        else:
                            print('\t>>> Please enter an integer greater than 0 but less than 20.')
                    except ValueError:
                        print('\t>>> Please enter a valid integer greater than 0 but less than 20.')
                    

                for j in range(int(num)):
                    
                    temp = {}
                    print('\t>>> Entering Ingredient ' + str(j+1))

                    for k in ['ingredientName','measurement','quantity']:
                        user_input = input('\t>>>    Enter ' + ((k + ' (in grams,kilograms, etc)') if (k=='measurement') else k) +  ': ')

                        if user_input == "exit":
                            print('\t>>> Nothing was added to the Recipe Manager.')
                            print(dic)
                            return
                        
                        if k == 'ingredientName':
                            if validate_ingredientname(user_input) == False:
                                while validate_ingredientname(user_input) == False:
                                    user_input = input('\t>>>    Enter a valid ' + k + ': ')
                        
                        if k == 'measurement':
                            if validate_measurement(user_input) == False:
                                while validate_measurement(user_input) == False:
                                    user_input = input('\t>>>    Enter a valid ' + k + ': ')

                        if k == 'quantity':
                            if validate_quantity(user_input) == False:
                                while validate_quantity(user_input) == False:
                                    user_input = input('\t>>>    Enter a valid ' + k + ': ')
                                    
                                    

                        temp[k] = user_input
                    dic[i].append(temp) 


            elif i == "Instructions":
                temp = {}
                print('\t>>> Enter instructions: ')
                print('\t>>> \tCharacter limit for each instruction: 100')


                while True:
                    try:
                        num = input('\t>>> How many instructions do you want to enter? ')
                        num = int(num)
                        if 0 < num < 20:
                            break
                        else:
                            print('\t>>> Please enter an integer greater than 0 but less than 20.')
                    except ValueError:
                        print('\t>>> Please enter a valid integer greater than 0 but less than 20.')
                
                j = 0
                while j < num:
                    user_input = input('\t>>> Enter instruction ' + str(j+1) + ': ')
                    temp[str(j+1)] = user_input
                    if len(user_input) > 100 or len(user_input) == 0:
                        print('\t>>> Instruction should be between 0 and 100 characters long')
                        continue
                    j += 1
                
                dic['Instructions'] = temp


            else:
                print('\t>>> Enter ' + i + ' (enter "exit" to cancel adding recipes)')
                user_input = input('\t>>> ')

                if i == 'Recipe Name':
                    if validate_ingredientname(user_input) == False:
                        while validate_ingredientname(user_input) == False:
                            user_input = input('\t>>> Enter a valid Recipe Name: ')
                if i == 'Recipe Author':
                    if validate_ingredientname(user_input) == False:
                        while validate_ingredientname(user_input) == False:
                            user_input = input('\t>>> Enter a valid Recipe Author: ')
                if i == 'Preparation time':
                    if validate_quantity(user_input) == False:
                        while validate_quantity(user_input) == False:
                            user_input = input('\t>>> Enter a valid Preparation time: ')
                
                if i == 'Cook time':
                    if validate_quantity(user_input) == False:
                        while validate_quantity(user_input) == False:
                            user_input = input('\t>>> Enter a valid Cook time: ')
                
                if i == 'Serving Size':
                    if validate_quantity(user_input) == False:
                        while validate_quantity(user_input) == False:
                            user_input = input('\t>>> Enter a valid Serving Size: ')
                

                if user_input == "exit":
                    print('Nothing was added to the Recipe Manager.')
                    print(dic)
                    return

                dic[i] = user_input

        print('\n')
        for i in dic:
            print(dic[i])

        print('\n\t>>>Do you want to add this recipe to Recipe Manager? y/n')

        user_input = input('\t>>>')

        if user_input not in ['y','n']:
            while user_input not in ['y','n']:
                print('\t>>>Do you want to add this recipe to Recipe Manager? y/n')
                user_input = input('\t>>>')
        
        if user_input == 'y':
            temp = sorted(rm.data, key = lambda x: x.id)
            
            if len(temp) == 0:
                id = 0
            else:
                id = temp[-1].id

            rm.addRecipe(Recipe(id+1,dic['Recipe Name'],dic['Recipe Author'],dic['Preparation time'],dic['Cook time'],dic['Serving Size'],dic['Ingredients'],dic['Instructions']))
            print('\t>>>' + dic['Recipe Name'] + ' by ' + dic['Recipe Author'] + ' added to Recipe Manager.')

        if user_input == 'n':
            print('\t>>>Nothing was added to the Recipe Manager.')

    def do_edit(self,arg):
        'Help text'
        pass

    def do_delete(self,arg):
        '\nWipes a recipe from the memory.\n\tCommand: delete <id>.\n'
        if arg:
            if arg.isnumeric():
                rm.deleteRecipe(int(arg))
                return
        print("\tCommand: delete <id>.\n")

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

    def do_clear(self,arg):
        '\nClears Recipe Manager\'s memory. \n\t Command: clear  \n Optional Argument: --f forces the clear without y/n \n'
        if arg == '--f':
            rm.data = []
            print('Recipe Manager memory cleared successfully.')
            print(rm.data)
        else:
            print('WARNING: Are you sure you want to clear Recipe Manager\'s data? (y/n)')



    def do_exit(self,arg):
        'Exits RmMode shell. \n\tCommand: exit\n'
        print('Thank you for using Recipe Manager!')

        return True


if __name__ == '__main__':
    RmMode().cmdloop()