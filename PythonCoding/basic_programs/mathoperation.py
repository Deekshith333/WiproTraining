from mypack.basicshapes import areaofsquare, areaofrect
from mypack.circle import areaofcircle, perimeterofcircle

radius = int(input('Enter radius : '))

print('Area : ', areaofcircle(rad=radius))
print('Peri : ', perimeterofcircle(rad=radius))

si = int(input('Enter side of sq : '))
print('Area : ', areaofsquare(side=si))
print('Peri : ', perimeterofsquare(side=si))

l = int(input('Enter length : '))
b = int(input('Enter breadth : '))
print('Area : ', areaofrect(l,b))
