import click
from Core.recipeProject import RecipeManager

rm = RecipeManager()


@click.group()
def cli():
    pass


@click.command()
def activate():
    click.echo("Welcome to Recipe Manager>")
    dic = {'add': rm.addRecipe, 'view': rm.viewRecipe, 'update': rm.updateRecipe, 'export': rm.exportRecipes, 'import': import_recipe}
    while True:
        user_input = click.prompt("RmMode>", prompt_suffix=" ")
        if user_input == "exit":
            click.echo("Exiting RmMode>")
            break
        if user_input not in ['add', 'view', 'update', 'delete', 'export', 'import']:
            click.echo("Invalid command. Type help for manual.")
        else:
            # Process user input or execute the desired commands
            click.echo(f"You entered: {user_input}")
            if user_input.startswith('import '):
                # Parse the command and argument
                command, arg = user_input.split(' ', 1)
                # Invoke the command with the argument
                dic[command](arg)
            else:
                dic[user_input]()


@click.command()
@click.argument('filename')
def import_recipe(filename):
    click.echo(f"Importing recipes from {filename}...")


# Define other commands (add_recipe, view_recipe, update_recipe, export_recipes) here

# Add the commands to the CLI
cli.add_command(activate)
cli.add_command(import_recipe)
# Add other commands to the CLI

if __name__ == '__main__':
    cli()