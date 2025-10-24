from Colors import Colors
from typing import Tuple, overload

class Printer:
    color: Colors
    position: Tuple[int, int]
    symbol: str


    def __init__(self, color: Colors, position: Tuple[int, int], symbol: str, font_path: str) -> None:
        self.color = color
        self.position = position
        self.symbol = symbol
        self.font_path = font_path
    
    @classmethod
    def load_font(self, font_path: str) -> list[list[str]]:
        letters = []

        with open(font_path) as file:
            height = int(file.readline())

            while True:
                lines = [file.readline() for _ in range(height)]
                letters.append(lines)

                if not lines[0]:
                    break
        
        return letters

    
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        return
    
    @classmethod
    def static_print(cls, text: str, color: Colors , position: Tuple[int, int], symbol: str, font_path: str) -> None:
        letters = Printer.load_font(font_path)
        height = len(letters[0])

        text = text.lower().strip()
        lines: list[str] = [''  for _ in range(height + position[1])]
        
        spec_letters = []

        if symbol == "*":
            spec_letters = letters
        else:
            for font in letters:
                font = [font[i].replace("*", symbol) for i in range(height)]
                spec_letters.append(font)

        is_first = True
        for letter in text:
            if is_first:
                for i in range(height):
                    if letter == " ":
                        lines[i + position[1]] += (' ' * 5)
                        continue
                    lines[i + position[1]] += (' ' * (position[0]) + color.value + spec_letters[ord(letter) - 97][i][:-1:] \
                        + "  " + Colors.DEFAULT.value)
                    is_first = False
            else:
                for i in range(height):
                    if letter == " ":
                        lines[i + position[1]] += (' ' * 5)
                        continue
                    lines[i + position[1]] += (color.value + spec_letters[ord(letter) - 97][i][:-1:] \
                        + "  " + Colors.DEFAULT.value)

        

        for line in lines:
            print(line)
    
    def print(self, text: str) -> None:
        letters = Printer.load_font(self.font_path)
        height = len(letters[0])

        text = text.lower().strip()
        lines: list[str] = [''  for _ in range(height + self.position[1])]
        
        spec_letters = []

        if self.symbol == "*":
            spec_letters = letters
        else:
            for font in letters:
                font = [font[i].replace("*", self.symbol) for i in range(height)]
                spec_letters.append(font)

        is_first = True
        for letter in text:
            if is_first:
                for i in range(height):
                    lines[i + self.position[1]] += (' ' * (self.position[0]) + self.color.value + spec_letters[ord(letter)\
                        - 97][i][:-1:] + "  " + Colors.DEFAULT.value)
                    is_first = False
            else:
                for i in range(height):
                    lines[i + self.position[1]] += (self.color.value + spec_letters[ord(letter) - 97][i][:-1:] \
                        + "  " + Colors.DEFAULT.value)
    
        for line in lines:
            print(line)

