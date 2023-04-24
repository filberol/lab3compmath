from commands.command import Command
from terminal_colors import *
import webbrowser


class ShowPic(Command):
    def __init__(self):
        Command.__init__(self)

    def execute_command(self, arguments):
        print_c("Showing functions in browser...", Colors.WARNING)
        webbrowser.open("functions.png")

    def __str__(self):
        return "Show available functions in gallery"
