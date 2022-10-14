# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

day = int(input('Enter day number: '))

if day > 7 or day < 0:
    print('Incorrect day number!')

if day == 6 or day == 7:
    print('Weekend!')

if day > 0 and day < 6:
    print('Weekday')
