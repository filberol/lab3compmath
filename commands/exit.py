from commands.command import Command


class Exit(Command):
    def __int__(self):
        Command.__init__(self)

    def execute_command(self, arguments):
        print("Exiting...")
        exit(0)

    def __str__(self):
        return "Exit programme without saving"
