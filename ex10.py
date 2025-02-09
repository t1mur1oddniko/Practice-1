flight = input("Введите номер рейса: ")
airlines_ru = input("Введите название авиакомпании на русском языке: ")
airlines_eng = input("Введите название авиакомпании на английском языке: ")
city_ru = input("Введите город прилёта на русском языке: ")
city_eng = input("Введите город прилета на английском языке: ")

print(f'Заканчивается посадка на рейс {flight} {airlines_ru} до {city_ru}')
print(f'This is the final boarding call for {airlines_eng} flight {flight} to {city_eng}')