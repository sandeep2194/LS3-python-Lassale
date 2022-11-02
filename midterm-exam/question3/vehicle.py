
from datetime import date


class Vehicle:
    # class level att
    count = 0

    def __init__(self, make, model, price, year):
        # Instance Level Att
        Vehicle.count += 1
        self.make = make
        self.model = model
        self.price = price
        self.year = year
        self.__vin_number = f'{make[0]}_{model[0]}_{str(year)}'

    def show_info(self):
        print('*****************')
        print(f'Make: {self.make}')
        print(f'Model: {self.model}')
        print(f'Price: {self.price}')
        print(f'Year: {self.year}')
        print(f'Vin Number: {self.__vin_number}')
        print('*****************')

    def get_vehicle_vin_number(self):
        return self.__vin_number
