# -*- coding: utf-8 -*-
"""
@author: Amaury Ortega <amauryocortega@gmail.com>
"""
from Data import DIGITS_STRUCTURE


class Digit(object):
    output = []
    digit = 0
    size = 0

    def __init__(self, size, digit):
        # Initializing properties of object
        self.size = size
        self.digit = digit
        # Filling output with B
        self.output = ["B" for line in range(self.getLines())]
        for line_index in range(self.getLines()):
            self.output[line_index] = self.getColumns() * "B"

        # Filling output optimized
        # TOP
        symbols = DIGITS_STRUCTURE.get(self.digit).get("TOP")
        self.output[0] = symbols[0] + symbols[1] * self.size + symbols[2]

        # FILL 1
        symbols = DIGITS_STRUCTURE.get(self.digit).get("FILL1")
        for line_index in range(1, self.getMiddleLine_Index()):
            self.output[line_index] = symbols[0] + symbols[1] * self.size + symbols[2]
        # MID
        symbols = DIGITS_STRUCTURE.get(self.digit).get("MID")
        self.output[self.getMiddleLine_Index()] = symbols[0] + symbols[1] * self.size + symbols[2]

        # FILL 2
        symbols = DIGITS_STRUCTURE.get(self.digit).get("FILL2")
        for line_index in range(self.getMiddleLine_Index() + 1, self.getLines()):
            self.output[line_index] = symbols[0] + symbols[1] * self.size + symbols[2]
        # BOT
        symbols = DIGITS_STRUCTURE.get(self.digit).get("BOT")
        self.output[self.getLines() - 1] = symbols[0] + symbols[1] * self.size + symbols[2]

    def getLines(self):
        return self.size * 2 + 3

    def getColumns(self):
        return self.size + 2

    def getMiddleLine_Index(self):
        return self.getLines() // 2

    def lcdNumber(self):
        return self.output
