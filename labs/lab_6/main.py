from Button import Button
from Serializer import Serializer
from KeyCommand import KeyCommand
from VolumeDownCommand import VolumeDownCommand
from VolumeUpCommand import VolumeUpCommand
from MediaPlayerCommand import MediaPlayerCommand
from Keyboard import Keyboard

button_up = Button("ctrl++", VolumeUpCommand(20))
button_down = Button("ctrl+-", VolumeDownCommand(20))
button_media = Button("ctrl+p", MediaPlayerCommand())

buttons = [button_down, button_up, button_media]

for letter in "qwertyuioplkjhgfdsazxcvbnm":
    buttons.append(Button(letter, KeyCommand(letter)))

keyboard = Keyboard(buttons)

while True:
    press = input()

    if press == "undo":
        keyboard.undo()
    elif press == "redo":
        keyboard.redo()
    elif press == "exit":
        break
    else:
        keyboard.handle_press(press)

keyboard.save()
    
