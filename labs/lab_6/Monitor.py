

class Monitor:
    def __init__(self, output_file: str) -> None:
        self._output_file = output_file

    def output_command(self, message: str) -> None:
        try:
            with open(self._output_file, "w+") as file:
                file.write(message)
        except:
            pass
    
    def output_symbol(self, message: str) -> None:
        try:
            with open(self._output_file, "a+") as file:
                file.write(message)
        except:
            pass
    
    def delete_last_symbol(self) -> None:
        try:
            with open(self._output_file, "r+") as file:
                current_text = file.read()
                try:
                    with open(self._output_file, "w+") as file:
                        file.write(current_text[:-1:])
                except:
                    return
        except:
            return