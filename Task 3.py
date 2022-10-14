# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).


x = int(input("x = "))
y = int(input("y = "))

if x > 0 and y > 0:
    print(f'x = {x} y = {y} This is first quarter')
if x < 0 and y > 0:
    print(f'x = {x} y = {y} This is second quarter')
if x < 0 and y < 0:
    print(f'x = {x} y = {y} This is third quarter')
if x > 0 and y < 0:
    print(f'x = {x} y = {y} This is forth quarter')
