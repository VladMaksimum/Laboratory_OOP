from Colors import Colors
from typing import Tuple, overload

HEIGHT = 7
FONT_SMALL = "labs/lab_2/small_fonts.txt"
FONT_BIG = "labs/lab_2/big_fonts.txt"
LETTETS = []
with open(FONT_BIG) as file:
    while True:
        lines = [file.readline() for _ in range(HEIGHT)]
        LETTETS.append(lines)

        if not lines[0]:
            break


class Printer:
    color: Colors
    position: Tuple[int, int]
    symbol: str


    def __init__(self, color: Colors, position: Tuple[int, int], symbol: str) -> None:
        self.color = color
        self.position = position
        self.symbol = symbol
    
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        return
    
    @classmethod
    def static_print(cls, text: str, color: Colors , position: Tuple[int, int], symbol: str) -> None:
        text = text.lower().strip()
        lines: list[str] = [''  for _ in range(HEIGHT + position[1] - 1)]
        
        spec_letters = []

        if symbol == "*":
            spec_letters = LETTETS
        else:
            for font in LETTETS:
                font = [font[i].replace("*", symbol) for i in range(HEIGHT)]
                spec_letters.append(font)


        for letter in text:
            for i in range(HEIGHT):
                lines[i + position[1] - 1] += (' ' * (position[0] - 1) + color.value + spec_letters[ord(letter) - 97][i][:-1:] \
                    + "  " + Colors.DEFAULT.value)

        

        for line in lines:
            print(line)
    
    def print(self, text: str) -> None:
        text = text.lower().strip()
        lines: list[str] = [''  for _ in range(HEIGHT + self.position[1] - 1)]
        
        spec_letters = []

        if self.symbol == "*":
            spec_letters = LETTETS
        else:
            for font in LETTETS:
                font = [font[i].replace("*", self.symbol) for i in range(HEIGHT)]
                spec_letters.append(font)


        for letter in text:
            for i in range(HEIGHT):
                lines[i + self.position[1] - 1] += (' ' * (self.position[0] - 1) + self.color.value + spec_letters[ord(letter) - 97][i][:-1:] \
                    + "  " + Colors.DEFAULT.value)

        

        for line in lines:
            print(line)

