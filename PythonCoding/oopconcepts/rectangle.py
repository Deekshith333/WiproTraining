from typing import override

from oopconcepts.formulamethoda import FM

class Rectangle(FM):
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    @override
    def calculate_area(self):
        return self.length * self.breadth

    @override
    def calculate_perimeter(self):
        return 2 * (self.length + self.breadth)