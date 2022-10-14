# Напишите программу, которая по заданному номеру четверти
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Enter quarter'))

if quarter == 1:
    print(f'Possible coordinated for  {quarter} are x (0, inf) y (0, inf)')
if quarter == 2:
    print(f'Possible coordinated for  {quarter} are x (0, -inf) y (0, inf)')
if quarter == 3:
    print(f'Possible coordinated for  {quarter} are x (0, -inf) y (0, -inf)')
if quarter == 4:
    print(f'Possible coordinated for  {quarter} are x (0, inf) y (0, inf)')
if quarter > 4:
    print('Enter number from 1 to 4')
