from EventHandler import EventHandler
from PropertyChangedEventArgs import PropertyChangedEventArgs

class PropetryChangedEventHandler(EventHandler[PropertyChangedEventArgs]):
    def handle(self, sender: object, args: PropertyChangedEventArgs) -> bool:
        print(f'In object {sender} someone tried to change property {args.prop_name}')
        return True