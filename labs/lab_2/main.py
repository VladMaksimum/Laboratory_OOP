from Printer import Printer
from Colors import Colors

with Printer(color=Colors.RED, position=(5,5), symbol="#", font_path="labs/lab_2/big_fonts.txt", interletters_space=5) as printer:
    printer.print("Hello")
    printer.print("hi")

Printer.static_print(text="Goodbye", color=Colors.GREEN, position=(10,3), symbol="@", font_path="labs/lab_2/small_fonts.txt", interletters_space=7)
Printer.static_print(text="The end", color=Colors.BLACK, position=(8,15), symbol= "&", font_path="labs/lab_2/big_fonts.txt", interletters_space=5)

