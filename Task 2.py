# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            first_part = not (x or y or z)
            second_part = not x and not y and not z
            result = first_part == second_part

if result is True:
    print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z is  true')
