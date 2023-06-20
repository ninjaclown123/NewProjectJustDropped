import copy
import os
import threading
import sys
from typing import IO
# from app import app
from werkzeug.serving import make_server

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException

#Flask imports
from flask import Flask, render_template, redirect, url_for, flash, request
from recipeProject import RecipeManager, Recipe
import logging, json
from tkinter import Tk, filedialog

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
    
    # def __init__(self):
    #     self.gui_status = False
    def __init__(self, completekey: str = "tab", stdin: IO[str] | None = None, stdout: IO[str] | None = None) -> None:
        super().__init__(completekey, stdin, stdout)
        self.gui_status = False
        self.server_thread = None
        self.server = None
        self.selenium_fail = False

    def do_view(self,arg):
        'Type in "view all" to view all the recipes OR type "view <id>" to view specific id! \nPrint a sorted list of recipes by recipe_name or recipe_author: \nview sort recipe_name \n view sort recipe_author'
        arg = str(arg)
        check = True
        if arg:
            args = arg.split()
            if args[0] == 'sort':
                if len(args) < 2:
                    print('\t>>>Sort argument not supplied! Consult manual: help view')
                    return
                
                if args[1] not in ['recipe_name' , 'recipe_author']:
                    print('\t>>>Sort argument not supplied! Consult manual: help view')
                    return
                
                if args[1] == 'recipe_name':
                    my_recipes = rm.data.copy()
                    my_sorted = sorted(my_recipes, key=lambda x: x.recipe_name)

                    rm.data = my_sorted
                    print('\t>>>Sorted by recipe name.\n')
                    rm.viewRecipeList()

                    # unsort the data.
                    rm.data = my_recipes
                    return
                if args[1] == 'recipe_author':
                    my_recipes = rm.data.copy()
                    my_sorted = sorted(my_recipes, key=lambda x: x.recipe_author)

                    # temporarily sort the data, then print it.
                    rm.data = my_sorted
                    print('\t>>>Sorted by recipe author.\n')
                    rm.viewRecipeList()

                    # unsort the data.
                    rm.data = my_recipes
                    return

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

        if self.gui_status:
            print('\t>>>Add command unavailable while GUI is active.')
            return

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

    def do_edit(self, arg):
        'Edit a recipe in Recipe Manager. Command: edit <id>'

        if self.gui_status:
            print('\t>>>Edit command unavailable while GUI is active.')
            return 

        if arg:
            if arg.isnumeric():
                recipe_id = int(arg)
                recipe = rm.viewSpecificRecipe(recipe_id)
                if recipe:
                    # Display the current recipe details
                    print(f"Editing Recipe: {recipe.recipe_name}")
                    print("Current Details:")
                    # Print the current details of the recipe
                    print(recipe)

                    # Prompt the user for new details
                    print("Enter new details (enter 'exit' to cancel):")
                    new_recipe = copy.deepcopy(recipe)  # Create a deep copy of the recipe to store the updated details

                    # Prompt the user for each field of the recipe and update it accordingly
                    for field in new_recipe.__dict__.keys():
                        if field == 'id':
                            continue
                        elif field == 'ingredients':
                            print("Enter new ingredients:")
                            new_ingredients = []
                            while True:
                                ingredient_name = input("Ingredient Name: ")
                                if ingredient_name == 'exit':
                                    break

                                measurement = input("Measurement: ")
                                if measurement == 'exit':
                                    break

                                quantity = input("Quantity: ")
                                if quantity == 'exit':
                                    break

                                if (
                                        validate_ingredientname(ingredient_name)
                                        and validate_measurement(measurement)
                                        and validate_quantity(quantity)
                                ):
                                    new_ingredients.append(
                                        {
                                            'ingredientName': ingredient_name,
                                            'measurement': measurement,
                                            'quantity': quantity
                                        }
                                    )
                                else:
                                    print("Invalid ingredient details. Please try again.")

                            new_recipe.ingredients = new_ingredients
                        elif field == 'instructions':
                            print("Enter new instructions:")
                            new_instructions = {}
                            while True:
                                instruction_number = input("Instruction Number: ")
                                if instruction_number == 'exit':
                                    break

                                instruction_text = input("Instruction Text: ")
                                if instruction_text == 'exit':
                                    break

                                if (
                                        instruction_number.isnumeric()
                                        and 0 < int(instruction_number) <= 20
                                        and 0 < len(instruction_text) <= 100
                                ):
                                    new_instructions[instruction_number] = instruction_text
                                else:
                                    print("Invalid instruction details. Please try again.")
                            new_recipe.instructions = new_instructions
                        else:
                            user_input = input(f"{field}: ")
                            if user_input == 'exit':
                                break

                            if field == 'recipe_name' and not validate_ingredientname(user_input):
                                print("Invalid recipe name. Please try again.")
                                continue

                            if field == 'preparation_time' and not validate_quantity(user_input):
                                print("Invalid preparation time. Please try again.")
                                continue

                            if field == 'cook_time' and not validate_quantity(user_input):
                                print("Invalid cook time. Please try again.")
                                continue

                            if field == 'serving_size' and not validate_quantity(user_input):
                                print("Invalid serving size. Please try again.")
                                continue

                            setattr(new_recipe, field, user_input)

                    # After updating the recipe, display the updated details
                    print("Updated Details:")
                    print(new_recipe)

                    # Ask the user if they want to save the changes
                    print("Save changes? (y/n)")
                    user_input = input(">>> ")
                    if user_input.lower() == 'y':
                        # Update the recipe in the Recipe Manager
                        rm.editRecipe(new_recipe)
                        print("Recipe updated successfully.")
                    else:
                        print("Changes discarded.")
                else:
                    print("Recipe not found.")
            else:
                print("Invalid recipe ID.")
        else:
            print("Command: edit <id>")

    def do_delete(self,arg):
        '\nWipes a recipe from the memory.\n\tCommand: delete <id>.\n'

        if self.gui_status:
            print('\t>>>Delete command unavailable while GUI is active.')
            return

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
        else:
            print('\t>>> Import command requires filename argument')

    def do_clear(self,arg):
        '\nClears Recipe Manager\'s memory. \n\t Command: clear  \n Optional Argument: --f forces the clear without y/n \n'

        if self.gui_status:
            print('>>>\tClear command unavailable while GUI is active.')

        if arg == '--f':
            rm.data = []
            print('Recipe Manager memory cleared successfully.')
            print(rm.data)
        else:
            print('\tWARNING: Are you sure you want to clear Recipe Manager\'s data? (y/n)')
            user_input = input('\t>>>')
            if user_input == 'y':
                rm.data = []
                print('\tRecipe Manager memory cleared successfully.')
            else:
                print('\tClear memory operation cancelled')


    def do_gui(self, arg):
        if arg == 'activate':
            if not self.gui_status:
                self.start_server()
                self.gui_status = True
                
                try:
                    self.chrome = webdriver.Chrome()
                    self.chrome.get('http://127.0.0.1:5000')
                except Exception as e:
                    self.selenium_fail = True
                    print(f"Selenium failed. Copy-paste this to your browser's URL or Ctrl + click this to open the GUI: 127.0.0.1:5000\n")
                


                print('GUI activated successfully.')
                return
            else:
                print('GUI is active.')

        elif arg == 'deactivate':
            if self.gui_status:
                user_prompt = input('\t>>> Are you sure you want to close the GUI? (y/n): ')
                if user_prompt not in ['y','n']:
                    while user_prompt not in ['y','n']:
                        user_prompt = input('\t>>> Are you sure you want to close the GUI? (y/n): ')

                if user_prompt == 'n':
                    return

                self.server.shutdown()
                self.server_thread.join()
                self.server_thread = None
                self.gui_status = False

                try:

                    if self.selenium_fail == False:
                        self.chrome.close()
                        # self.chrome.find_element(By.XPATH,"//div[@class='recipe-list']/ul/li/a[@href='/view/0']")
                    
                except NoSuchWindowException:
                    print("\t>>> GUI was closed.")
                except Exception as e:
                    print("\t>>> GUI was closed.")


                    

                print('\t>>> GUI deactivated successfully.')
                return
            else:
                print('\t>>> GUI is inactive.')
                return
        else:
            print('\t>>> Invalid argument provided. Consult manual: help gui')

    def start_server(self):
        if self.gui_status:
            print('\t>>> GUI is active.')
            return
        else:
            # server = make_server('127.0.0.1', 5000, app)
            # server.serve_forever()

            self.server = make_server('127.0.0.1', 5000, app)
            self.server_thread = threading.Thread(target=self.server.serve_forever)
            self.server_thread.start()

    def do_exit(self,arg):
        'Exits RmMode shell. \n\tCommand: exit\n'
        if self.gui_status:
            print('\t>>> GUI is still active. Exit GUI command: gui deactivate')
            return

        print('\t>>> Thank you for using Recipe Manager!')

        return True


app = Flask(__name__)

# logging.basicConfig(filename='gui_logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# rm = RecipeManager()
nameSort = True
idSort = True
authorSort = True
totalSort = True
servingSort = True

@app.route('/')
def home():
    recipe_list = rm.RecipeList()
    return render_template('index.html', recipe_list=recipe_list)

@app.route('/sortID')
def sortID():
    global idSort
    idSort = not idSort
    recipe_list = sorted(rm.RecipeList(), key = lambda x: x.id, reverse = idSort)

    return render_template('index.html', recipe_list=recipe_list)

@app.route('/view/<id>')
def view_id(id):
    recipe = rm.viewSpecificRecipe(int(id))
    # print(rm.data)
    return render_template('viewID.html', recipe = recipe)

@app.route('/add', methods=['GET'])
def add():
    temp = []
    for i in rm.RecipeList():
        temp.append(i.recipe_name)
    return render_template('add.html',recipe = Recipe(
            0,
            "McBurger",
            "Sam",
            10,
            12,
            1,
            [
                {"ingredientName": "bun", "quantity": 1, "measurement": "unit"},
            ],
            {
                "1": "Assemble the bun and the secret patty.",

            }
        ),recipe_list = temp
        )

@app.route('/save_recipe', methods=['POST'])
def save_recipe():
    recipe_name = request.form.get('recipe_name')
    recipe_author = request.form.get('recipe_author')
    prep_time = int(request.form.get('prep_time'))
    cook_time = int(request.form.get('cook_time'))
    serving_size = int(request.form.get('serving_size'))
    
    ingredient_names = request.form.getlist('ingredient_name[]')
    ingredient_quantities = request.form.getlist('ingredient_quantity[]')
    ingredient_measurements = request.form.getlist('ingredient_measurement[]')
    
    ingredients = []
    for name, quantity, measurement in zip(ingredient_names, ingredient_quantities, ingredient_measurements):
        ingredient = {
            'ingredientName': name,
            'quantity': int(quantity),
            'measurement': measurement
        }
        ingredients.append(ingredient)
    
    instruction_texts = request.form.getlist('instruction[]')
    
    instructions = {}
    for i, text in enumerate(instruction_texts, start=1):
        instructions[str(i)] = text
    
    temp = sorted(rm.data, key = lambda x: x.id)
    # print(temp[-1].id,recipe_name,recipe_author,prep_time,cook_time,serving_size,ingredients,instructions)
    try:
        rm.addRecipe(Recipe(temp[-1].id+1,recipe_name,recipe_author,prep_time,cook_time,serving_size,ingredients,instructions))
    except Exception as e:
        print(e)
        return redirect(url_for('home'))
    
    return redirect(url_for('home'))


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_id(id):
    # Find the recipe with the given id in the recipe list
    recipe = None
    for r in rm.RecipeList():
        if r.id == id:
            recipe = r
            break

    if recipe is None:
        # Handle the case when the recipe is not found
        flash("Recipe not found.")
        return redirect(url_for('home'))

    if request.method == 'POST':
        # Update the recipe with the submitted form data
        recipe.recipe_name = request.form.get('recipe_name')
        recipe.recipe_author = request.form.get('recipe_author')
        recipe.prep_time = request.form.get('prep_time')
        recipe.cook_time = request.form.get('cook_time')
        recipe.serving_size = request.form.get('serving_size')

        # Debugging: Print the form inputs
        print("Recipe Name:", recipe.recipe_name)
        print("Author:", recipe.recipe_author)
        print("Preparation Time:", recipe.prep_time)
        print("Cook Time:", recipe.cook_time)
        print("Serving Size:", recipe.serving_size)

        # Update ingredients
        ingredients = []
        i = 0
        while f'ingredient_name_{i}' in request.form:
            ingredient_name = request.form.get(f'ingredient_name_{i}')
            ingredient_quantity = request.form.get(f'ingredient_quantity_{i}')
            ingredient_measurement = request.form.get(f'ingredient_measurement_{i}')
            ingredients.append({
                "ingredientName": ingredient_name,
                "quantity": ingredient_quantity,
                "measurement": ingredient_measurement
            })
            i += 1

        recipe.ingredients = ingredients

        # Debugging: Print the ingredients
        print("Ingredients:", recipe.ingredients)

        # Update instructions
        instructions = {}
        i = 0
        while f'instruction_{i}' in request.form:
            instruction = request.form[f'instruction_{i}']
            instructions[i + 1] = instruction
            i += 1
        recipe.instructions = instructions

        # Debugging: Print the instructions
        print("Instructions:", recipe.instructions)

        return redirect(url_for('view_id', id=id))

    return render_template('edit.html', recipe=recipe)


@app.route('/delete/<id>')
def delete_id(id):
    recipe_name = rm.viewSpecificRecipe(int(id)).recipe_name
    return render_template('index.html', recipe_list=rm.RecipeList(), recipe_name=recipe_name, recipe_id=id)

@app.route('/deleteConfirm/<id>')
def deleteConfirm_id(id):
    rm.deleteRecipe(int(id))
    return render_template('index.html', recipe_list=rm.RecipeList())

@app.route('/sortRecipeName')
def sortRecipeName():
    global nameSort
    nameSort = not nameSort
    recipe_list = sorted(rm.RecipeList(), key = lambda x: x.recipe_name, reverse = nameSort)
    return render_template('index.html', recipe_list=recipe_list)

@app.route('/sortRecipeAuthor')
def sortRecipeAuthor():
    global authorSort
    authorSort = not authorSort
    recipe_list = sorted(rm.RecipeList(), key = lambda x: x.recipe_author, reverse=authorSort)
    return render_template('index.html', recipe_list=recipe_list)

@app.route('/sortTotalTime')
def sortRecipeTotalTime():
    global totalSort
    totalSort = not totalSort
    recipe_list = sorted(rm.RecipeList(), key = lambda x: (x.prep_time+x.cook_time), reverse=totalSort)
    return render_template('index.html', recipe_list=recipe_list)

@app.route('/sortServingSize')
def sortRecipeServingSize():
    global servingSort
    servingSort = not servingSort
    recipe_list = sorted(rm.RecipeList(), key = lambda x: (x.serving_size), reverse=servingSort)
    return render_template('index.html', recipe_list=recipe_list)


@app.route('/exit')
def exitGUI():
    pass
    
@app.route('/export')
def export():
    root = Tk()
    root.attributes('-topmost', True)
    root.withdraw()


    file_name = filedialog.asksaveasfilename(title="Save recipes", defaultextension=".json",filetypes=[("JSON Files", "*.json")], initialfile='myJSON')

    if file_name:
        file = open(file_name, "w")
        json.dump(rm.exportRecipesGUI(), file, indent=4)
        file.close()

    root.destroy()

    return redirect(url_for('home'))

@app.route('/import')
def import_file():
    root = Tk()
    root.attributes('-topmost', True)
    root.withdraw()

    my_file = filedialog.askopenfilename(title="Import recipes", filetypes=[("JSON Files", "*.json")])

    if my_file:
        rm.importRecipesGUI(my_file)

    root.destroy()
    return redirect(url_for('home'))



if __name__ == '__main__':
    RmMode().cmdloop()