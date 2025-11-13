from EventHandler import EventHandler
from PropertyChangedEventArgs import PropertyChangedEventArgs
from typing import Generic, TypeVar

TEventArgs = TypeVar("TEventArgs")

class PropetryChangedEventHandler(Generic[TEventArgs], EventHandler[PropertyChangedEventArgs]):
    def handle(self, sender: object, args: PropertyChangedEventArgs) -> None:
        if isinstance(args, PropertyChangedEventArgs):
            print(f'In object {sender} someone tried to change property {args.prop_name}')