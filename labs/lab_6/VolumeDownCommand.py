from Command import Command

class VolumeDownCommand(Command):
    def __init__(self, volume_shift: int) -> None:
        self._volume_shift = volume_shift

    def do_command(self) -> None:
        try:
            with open("labs/lab_6/test.txt", "w") as file:
                file.write(f"volume decreased -{self._volume_shift}%")
        except:
            return
    
    def undo(self) -> None:
        try:
            with open("labs/lab_6/test.txt", "w+") as file:
                file.write(f"volume increased +{self._volume_shift}%")
        except:
            return
    
    def redo(self) -> None:
        self.do_command()