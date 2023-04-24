from commands.command import Command
from terminal_colors import *


class ListFunctions(Command):
    def __init__(self, manager):
        Command.__init__(self, manager)

    def execute_command(self, arguments):
        print_c("Functions available:", Colors.UNDERLINE)
        for index, func in enumerate(self.service.get_functions()):
            print_c(f"{index + 1}. f(x) = {func}", Colors.OKCYAN)

    def __str__(self):
        return "List available functions"
