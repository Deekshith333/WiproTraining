from typing import override

from oopconcepts.formulamethoda import FM

class Square(FM):
    def __init__(self, s):
        self.side = s

    @override
    def calculate_area(self):
        return self.side * self.side

    @override
    def calculate_perimeter(self):
        return 4 * self.side
