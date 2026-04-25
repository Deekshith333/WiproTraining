from oopconcepts.square import Square
from oopconcepts.rectangle import Rectangle

sqobj = Square(10)

print(f'Area: {sqobj. calculate_area()} \t Perimeter: {sqobj.calculate_perimeter()}')

rectobj = Rectangle(10, 5)
print(f'Area: {rectobj.calculate_area()} \t Perimeter: {rectobj.calculate_perimeter()}')
