from Printer import Printer
from Colors import Colors

with Printer(color=Colors.RED, position=(5,5), symbol="#") as printer:
    printer.print("Hello")

Printer.static_print(text="Goodbye", color=Colors.RED, position=(5,5), symbol="#")

