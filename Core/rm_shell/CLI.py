from Core.recipeProject import RecipeManager
import cmd


rm = RecipeManager()


class RmMode(cmd.Cmd):
    intro = 'Welcome to Recipe Manager!'
    prompt = 'RmMode> '

    def do_export(self, arg):
        'Export current recipe data in memory to a JSON file in Core/exports directory. Command: export'
        rm.exportRecipes()

    def do_import(self,arg):
        'Import a JSON file containing recipe data for Recipe Manager. Command: import <filename>'
        if arg:
            if arg[-(len(arg)-arg.index('.')):] != '.json':
                print(str(arg[-(len(arg)-arg.index('.')):]),'files are unacceptable. Please import a valid JSON file.')
            else:
                if arg[-5:] == '.json':
                    arg = arg[:-5]

                rm.importRecipes(arg)

    def do_exit(self,arg):
        'Exits RmMode shell. Command: exit'
        print('Thank you for using Recipe Manager!')

        return True


if __name__ == '__main__':
    RmMode().cmdloop()