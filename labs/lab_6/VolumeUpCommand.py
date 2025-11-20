from CommandWithMonitor import CommandWithMonitor

class VolumeUpCommand(CommandWithMonitor):
    def __init__(self, volume_shift: int) -> None:
        super().__init__()
        self._volume_shift = volume_shift

    def do_command(self) -> None:
        self._monitor.output_command(f"volume increased +{self._volume_shift}%")
    
    def undo(self) -> None:
        self._monitor.output_command(f"volume decreased -{self._volume_shift}%")
    
    def redo(self) -> None:
        self.do_command()