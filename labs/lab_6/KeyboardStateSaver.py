from pathlib import Path
from typing import Any
from Command import Command
import json
from Serializer import Serializer

OUTPUT_FILE = "labs/lab_6/test.txt"
STATE_SAVE_FILE = "labs/lab_6/state.json"

class KeyboardStateSaver:
    def __init__(self) -> None:
        self._serializer = Serializer()
        self._redo_stack: list[Command] = []
        self._history: list[Command] = []
        self._current_state_index = -1
        self._is_chain = True
        self._chain = ''

    def add_history(self, cmd: Command) -> None:
        self._history.append(cmd)
    
    def save_undo_cmd(self, cmd: Command) -> None:
        self._redo_stack.append(cmd)
        self._current_state_index -= 1

    def get_undo_cmd(self) -> Command | None:
        if self._current_state_index > 0:
            return self._history[self._current_state_index]
        
        return None
    
    def get_redo_cmd(self) -> Command | None:
        if self._redo_stack != []:
            self._current_state_index = len(self._history) - 1
            return self._redo_stack.pop()
        
        return None
    
    def move_index_forward(self) -> None:
        self._current_state_index += 1
    
    def move_index_back(self) -> None:
        self._current_state_index -= 1
    
    def switch_to_chain(self) -> None:
        try:
            with open(OUTPUT_FILE, "w") as file:
                file.write(self._chain)
        except:
            pass
    
    def update_chain(self) -> None:
        try: 
            with open(OUTPUT_FILE) as file:
                self._chain = file.read()
        except:
            pass
    
    def save(self, obj: Any) -> None:
        try:
            with open(STATE_SAVE_FILE, "w") as file:
                json.dump(obj, file, default=self._serializer._encode, indent=4)
        except:
            pass
    
    def load(self) -> Any:
        try:
            with open(STATE_SAVE_FILE) as file:
                return json.load(file, object_hook=self._serializer._decode, indent=4)
        except:
            pass

