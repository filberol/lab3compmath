class StateManager:
    __commands = None

    def __init__(self, functions):
        self.__functions = functions

    def get_functions(self):
        return self.__functions

    def get_commands(self):
        return self.__commands

    def set_commands(self, comm_list):
        self.__commands = comm_list
