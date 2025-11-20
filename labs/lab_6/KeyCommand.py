from CommandWithMonitor import CommandWithMonitor


class KeyCommand(CommandWithMonitor):
    def __init__(self, key: str) -> None:
        super().__init__()
        self._key = key

    def do_command(self) -> None:
        self._monitor.output_symbol(self._key)
    
    def undo(self) -> None:
        self._monitor.delete_last_symbol()
    
    def redo(self) -> None:
        self.do_command()