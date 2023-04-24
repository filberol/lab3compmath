from commands.command import Command
from terminal_colors import *


class ShowCommands(Command):
    def __init__(self, manager):
        Command.__init__(self, manager)

    def execute_command(self, arguments):
        print_c("Commands available:", Colors.UNDERLINE)
        commands = self.service.get_commands()
        for c_key in commands.keys():
            print_c(f'"{c_key}" - {commands[c_key]}', Colors.OKCYAN)

    def __str__(self):
        return "Show available commands with explanations"
