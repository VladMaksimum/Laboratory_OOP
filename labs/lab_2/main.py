from Printer import Printer
from Colors import Colors

with Printer(color=Colors.RED, position=(5,5), symbol="#") as printer:
    printer.print("Hello")

