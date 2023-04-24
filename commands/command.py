class Command:
    def __init__(self, state_manager=None):
        self.service = state_manager

    def execute_command(self, arguments):
        print("This command was not yet implemented.")
        print(self.service)

    def __str__(self):
        return "Basic command interface"
