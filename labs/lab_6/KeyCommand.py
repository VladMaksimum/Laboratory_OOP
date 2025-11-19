from Command import Command


class KeyCommand(Command):
    def __init__(self, key: str) -> None:
        self._key = key

    def do_command(self) -> None:
        try:
            with open("labs/lab_6/test.txt", "a+") as file:
                file.write(self._key)
        except:
            pass
    
    def undo(self) -> None:

        try:
            with open("labs/lab_6/test.txt", "r+") as file:
                current_text = file.read()
                try:
                    with open("labs/lab_6/test.txt", "w+") as file:
                        file.write(current_text[:-1:])
                except:
                    return
        except:
            return
    
    def redo(self) -> None:
        self.do_command()