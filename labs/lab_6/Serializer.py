from typing import Dict, Any
from Button import Button
from Command import Command
from KeyCommand import KeyCommand
from VolumeUpCommand import VolumeUpCommand
from VolumeDownCommand import VolumeDownCommand
from MediaPlayerCommand import MediaPlayerCommand
import json

class Serializer:
    @classmethod
    def _encode(self, obj: object) -> Dict[str, Any]:
        if isinstance(obj, Command):
            return {"__Command__": {"__type__": f"__{obj.__class__.__name__}__", "parameters": obj.__dict__}}
        
        return {f'__{obj.__class__.__name__}__': obj.__dict__}

    @classmethod
    def to_dict(self, obj: object) -> str:
        return (json.dumps(obj, default=self._encode))
    
    @classmethod
    def _decode(self, data_dict: Dict[str, Any]) -> Any:
        if '__Keyboard__' in data_dict:
            from Keyboard import Keyboard
            tmp_key = Keyboard()
            tmp_key.__dict__.update(data_dict['__Keyboard__'])
            return tmp_key
        
        elif '__Button__' in data_dict:
            tmp_but = Button()
            tmp_but.__dict__.update(data_dict['__Button__'])
            return tmp_but
        
        elif '__Command__' in data_dict:
            cmd = self._command_fabric(data_dict['__Command__']['__type__'], data_dict['__Command__']['parameters'])
            return cmd
        
        elif '__KeyboardStateSaver__' in data_dict:
            from KeyboardStateSaver import KeyboardStateSaver
            tmp_saver = KeyboardStateSaver()
            tmp_saver.__dict__.update(data_dict['__KeyboardStateSaver__'])
            return tmp_saver
        
        return data_dict


    @classmethod
    def from_dict(self, data_dict: str) -> Any:
        return json.loads(data_dict, object_hook=self._decode)
    
    @classmethod
    def _command_fabric(self, cmd_name: str, cmd_parametr: Any) -> Command | None:
        if cmd_name == "__KeyCommand__":
            return KeyCommand(cmd_parametr["_key"])
        
        elif cmd_name == "__MediaPlayerCommand__":
            tmp_player = MediaPlayerCommand()
            tmp_player._is_launched = cmd_parametr["_is_launched"]
            return tmp_player
        
        elif cmd_name == "__VolumeUpCommand__":
            return VolumeUpCommand(cmd_parametr["_volume_shift"])
        
        elif cmd_name == "__VolumeDownCommand__":
            return VolumeDownCommand(cmd_parametr["_volume_shift"])

        return None
        