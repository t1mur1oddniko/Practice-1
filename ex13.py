import math as m

print('Введите радиус "слепой зоны" и радиус дальности приёма: ')
radius1 = float(input())
radius2 = float(input())
range = abs((m.pi * (radius1 ** 2)) - (m.pi * (radius2 ** 2)))

print(f"Площадь покрываемой территории: {range}")