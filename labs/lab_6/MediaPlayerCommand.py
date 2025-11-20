from CommandWithMonitor import CommandWithMonitor


class MediaPlayerCommand(CommandWithMonitor):
    def __init__(self) -> None:
        super().__init__()
        self._is_launched = False

    def do_command(self) -> None:
        if self._is_launched:
            self._monitor.output_command("media player closed")
            self._is_launched = False
            return
        
        self._is_launched = True
        self._monitor.output_command("media player launched")
    
    def undo(self) -> None:
        self.do_command()
    
    def redo(self) -> None:
        self.do_command()
