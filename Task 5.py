# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
import math
Ax = int(input('Ax '))
Ay = int(input('Ay '))
Bx = int(input('Bx '))
By = int(input('By '))
result = math.sqrt((Ax-Bx)**2+(Ay-By)**2)

print(f' Dsitance : {result}')
