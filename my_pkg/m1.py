
# from functools import reduce


# list1 = []
# count = 0
# while count < 4:
#     x = float(input("Enter a float number:"))
#     count += 1
#     if isinstance(x, float):
#         list1.append(x)
#     else:
#         print("* YOUR VALUE IS NOT CORRECT TRY AGAIN **")


# def largest_number(x, y):
#     if x < y:
#         return y
#     else:
#         return x


# biggest_number = reduce(largest_number, list1)
# print(biggest_number)


class Vehicle:
    vehicle_count = 0

    def _init_(self, make, model, price, year):
        vehicle_count += 1
        self.make = make
        self.model = model
        self.price = price
        self.year = year

    def show_info(self):
        print("Make: ", self.make)
        print("Model: ", self.model)
        print("Price: ", self.price)
        print("Year: ", self.year)

    def get_vehicle_vin_number(self):
        VIN_number = self.make[0] + '_' + self.model[0] + '_' + self.year
        return VIN_number
