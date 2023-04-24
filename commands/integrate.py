from commands.command import Command
from terminal_colors import *
from integrator import trapezoid
from integrator.time_manager import time_count


class Integrate(Command):

    __def_segments = 10000

    # 0 function number
    # 1 borders
    # 2 number of segments
    @time_count
    def execute_command(self, arguments):
        if len(arguments) < 2:
            print_c(
                f"Usage: -> integrate <function No> <left b>:<right b> <segments(default {self.__def_segments})>",
                Colors.WARNING
            )
            return
        if int(arguments[0]) not in range(1, len(self.service.get_functions()) + 1):
            print_c("Invalid function index!", Colors.FAIL)
            return

        try:
            method = trapezoid.TrapezoidMethod()
            borders = list(map(lambda x: float(x), arguments[1].split(":")))
            function = self.service.get_functions()[int(arguments[0]) - 1]
            segments = float(arguments[2]) if len(arguments) > 2 else self.__def_segments
        except ValueError:
            print_c("Wrong arguments!", Colors.FAIL)
            return

        try:
            answer = method.solve(function, borders, segments)
            print(f"{method}: {answer} segmented by {int(segments)}")
        except ValueError:
            print_c("Calculation error", Colors.FAIL)
