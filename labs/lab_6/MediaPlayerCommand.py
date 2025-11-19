from Command import Command


class MediaPlayerCommand(Command):
    def __init__(self) -> None:
        self._is_launched = False

    def do_command(self) -> None:
        if self._is_launched:
            try:
                with open("labs/lab_6/test.txt", "w") as file:
                    file.write("media player closed")
                    self._is_launched = False
                    return
            except:
                return

        try:
            with open("labs/lab_6/test.txt", "w") as file:
                file.write("media player launched")
                self._is_launched = True
        except:
            return
    
    def undo(self) -> None:
        self.do_command()
    
    def redo(self) -> None:
        self.do_command()
