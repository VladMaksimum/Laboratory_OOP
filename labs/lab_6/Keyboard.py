from Button import Button
from KeyboardStateSaver import KeyboardStateSaver
from KeyCommand import KeyCommand
from typing import Self

class Keyboard:
    def __init__(self, buttons: list[Button] = []) -> None:
        self._buttons = buttons
        self._saver = KeyboardStateSaver()

    def set_button(self, button: Button) -> None:
        self._buttons.append(button)
    
    def update_button(self, new_button: Button) -> None:
        for button in self._buttons:
            if button._combination == new_button._combination:
                button = new_button
                return
    
    def handle_press(self, combination: str) -> None:
        for button in self._buttons:
            if button._combination == combination:
                if isinstance(button._command, KeyCommand):
                    if not self._saver._is_chain:
                        self._saver.switch_to_chain()
                        self._saver._is_chain = True

                    button.execute()
                    self._saver.update_chain()

                    self._saver.add_history(button._command)
                    self._saver.move_index_forward()
                    return
                
                if self._saver._is_chain:
                    self._saver.update_chain()

                button.execute()

                self._saver.add_history(button._command)
                self._saver.move_index_forward()
                self._saver._is_chain = False
                return

    def undo(self) -> None:
        cmd = self._saver.get_undo_cmd()

        if cmd != None:
            self._saver.save_undo_cmd(cmd)
            cmd.undo()
    
    def redo(self) -> None:
        cmd = self._saver.get_redo_cmd()

        if cmd != None:
            cmd.redo()
    
    def save(self) -> None:
        self._saver.save(self)
    
    def load(self) -> Self:
        return self._saver.load()


