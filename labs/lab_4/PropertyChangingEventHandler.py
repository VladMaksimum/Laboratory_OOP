from EventHandler import EventHandler
from PropertyChangingEventArgs import PropertyChangingEventArgs

class PropertyChangingEventHandler(EventHandler[PropertyChangingEventArgs]):
    def handle(self, sender: object, args: PropertyChangingEventArgs) -> bool:
        if not args.can_change:
            sender.__dict__[args.prop_name] = args.old_value
            print(f'Changing property {args.prop_name} in object {sender} from {args.old_value} to {args.new_value} was cancelled')
            return False

        print(f'Property {args.prop_name} in object {sender} was changed from {args.old_value} to {args.new_value}')
        return True
        