from math import *
#1
def degree_to_radian(degree):
    return radians(degree)
#print(degree_to_radian(int(input())))

#2
def area_of_trapezoid(h, a, b):
    area = h * 1/2 * (a + b)
    return area
#h = float(input('Height: '))
#a = float(input('Base, first value: '))
#b = float(input('Base, second value: '))
#print('Expected output:', area_of_trapezoid(h,a,b))

#3
def area_of_poligon(n, l):
    area = (n * l ** 2) / (tan( pi /n) * 4)
    return area
#n = int(input('Input number of sides: '))
#l = float(input('Input the length of a side: '))
#print('The area of the polygon is:', int(area_of_poligon(n,l)))

#4
def area_of_parallelogram(l, h):
    area = l * h
    return area
#l = float(input('Length of base: '))
#h = float(input('Height of parallelogram: '))
#print('Expected Output:', area_of_parallelogram(l,h))
