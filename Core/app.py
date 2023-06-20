
import json

from flask import Flask, render_template, redirect, url_for, flash, request


from recipeProject import RecipeManager, Recipe
import logging, json
from tkinter import Tk, filedialog

app = Flask(__name__)

# logging.basicConfig(filename='gui_logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

rm = RecipeManager()
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
        return redirect(url_for('index'))

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


    file_name = filedialog.asksaveasfilename(title="Save recipes", defaultextension=".json")

    if file_name:
        file = open(file_name, "w")
        json.dump(rm.exportRecipesGUI(), file, indent=4)
        file.close()

    root.destroy()

    return render_template('index.html', recipe_list=rm.RecipeList())

if __name__ == '__main__':
    app.run()
