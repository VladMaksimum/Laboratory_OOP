from Command import Command

class Button:
    def __init__(self, keys_combination: str = '', command: Command | None = None) -> None:
        self._combination = keys_combination
        self._command = command
    
    def set_command(self, cmd: Command) -> None:
        self._command = cmd
    
    def execute(self) -> None:
        if self._command != None:
            self._command.do_command()