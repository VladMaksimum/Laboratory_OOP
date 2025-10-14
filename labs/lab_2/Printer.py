from Colors import Colors
from typing import Tuple, List

class Printer:
    letters: List[List[str]]
    height: int
    color: Colors
    position: Tuple[int, int]
    symbol: str
    fonts_path: str = "labs/lab_2/small_fonts.txt"


    def __init__(self, color: Colors, position: Tuple[int, int], symbol: str) -> None:
        self.letters = []
        self.color = color
        self.position = position
        self.symbol = symbol

        with open(self.fonts_path) as file:
            self.height = int(file.readline())
            for _ in range(26):
                self.letters.append([file.readline().replace("*", self.symbol) for i in range(self.height)])


    @classmethod
    def print(self, text: str, color: Colors, position: Tuple[int, int], symbol: str) -> None:
        text = text.lower().strip()
        lines = [] * self.height

        for letter in text:
            for i in range(self.height):
                lines[i] += self.letters[ord(letter)][i][:-2:] + "  "
        

        map(print, lines)
            
