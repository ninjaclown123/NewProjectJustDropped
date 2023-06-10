import os
import click

print(os.getcwd())

from Core.recipeProject import RecipeManager



@click.command()

def hello():
    click.echo('Bruh')

if __name__ == '__main__':
    hello()