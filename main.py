from commands import *
from functions import *
from service import StateManager
from terminal_colors import *


def read_command(command_dict):
    input_line = input("-> ").split(" ")
    command_line = input_line.pop(0)
    try:
        command_dict[command_line].execute_command(input_line)
    except KeyError:
        print_c("Unknown command.", Colors.FAIL)


if __name__ == '__main__':
    functions = [
        cos.CosFunc(),
        sin.SinFunc(),
        log.LogFunc(),
        sqrt.SqrtFunc()
    ]
    manager = StateManager(functions)
    commands = {
        "exit": exit.Exit(),
        "show": show.ShowPic(),
        "list": list.ListFunctions(manager),
        "help": comm_list.ShowCommands(manager),
        "integrate": integrate.Integrate(manager)
    }
    manager.set_commands(commands)
    while True:
        read_command(commands)
