from flask import Flask, render_template, flash
from Core.recipeProject import RecipeManager
import logging

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

@app.route('/add')
def add():
    return render_template('add.html',recipe = {'Recipe Name':None, 'Recipe Author':None, 'Preparation time':None,'Cook time':None,'Serving Size':None,'Ingredients':[], 'Instructions':{}})
    

@app.route('/edit/<id>')
def edit_id(id):
    return render_template('edit.html',id = id)

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





if __name__ == '__main__':
    app.run()
