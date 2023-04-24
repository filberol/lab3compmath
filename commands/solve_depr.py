from commands.command import Command
from terminal_colors import *
from solver import half_split, chord


class SolveFunction(Command):
    def __init__(self, manager):
        Command.__init__(self, manager)

    __def_accuracy = 0.00001

    # args:
    # 1 - function number
    # 2 - borders left:right
    # 3 - accuracy
    def execute_command(self, arguments):
        if len(arguments) < 2:
            print_c(
                f"Usage: -> solve <function No> <left b>:<right b> <accuracy(default {self.__def_accuracy})>",
                Colors.WARNING
            )
            return
        if int(arguments[0]) > len(self.service.get_functions()) or int(arguments[0]) <= 0:
            print_c("Invalid function index!", Colors.FAIL)
            return

        try:
            methods = [half_split.HalfSplitMethod(), chord.ChordMethod()]
            borders = list(map(lambda x: float(x), arguments[1].split(":")))
            function = self.service.get_functions()[int(arguments[0]) - 1]
            accuracy = float(arguments[2]) if len(arguments) > 2 else self.__def_accuracy
        except ValueError:
            print_c("Wrong arguments!", Colors.FAIL)
            return

        try:
            for method in methods:
                answer = method.solve(function, borders, accuracy)
                print(f"{method}: {answer[0]} with _x_ accuracy of {accuracy}, {answer[1]} iterations")
        except ValueError:
            print_c("No solutions on interval, or function only touching null", Colors.FAIL)
