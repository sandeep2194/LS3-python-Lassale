import time
class Vehicle:
    ### class level att
    count=0
    __vin_number_prefix = 'VIN-'+f'{time.time_ns()}-'
    def __init__(self,brand, nd = 2, pr = 10000, yb = 1900):
        ### Instance Level Att
        Vehicle.count+=1
        self.speed=0
        self.__number_of_doors = nd ## private attr
        self.__price = pr
        self.__year_of_build = yb
        self.__plate_number = self.create_plate()
        self.__vin_number=Vehicle.__vin_number_prefix + brand
        
        self.brand=brand # public attribute
    ### list of methods

    @classmethod
    def show_total_vehicles(self):
        print(f"Total number of Vehicle is {Vehicle.count}.")
    ### instance level methods
    def start_engine(self):
        print('The Vehicle engine has been started.')
    def accelrate(speed):
        speed=speed
        print(f'speed is up{speed}')
    def create_plate(self):
        return f"QC-{self.__year_of_build}-{Vehicle.count}"
    def show_vehicle_info(self):
        print(f"This Vehicle ({self.__plate_number}) has {self.__number_of_doors} doors and its price is {self.__price}$.")
    ### getters and setters
    def get_price(self):
        return self.__price
    def set_price(self,pr):
        if pr < 10000:
            print(f'{pr} is not valid price.')
        else:
            self.__price = pr
    def get_number_of_doors(self):
        return self.__number_of_doors
    def set_number_of_doors(self, nd):
        if nd < 0:
            print(f'{nd} is NOT valid number of doors.')
        else:
            self.__number_of_doors = nd         
    def get_year_of_build(self):
        return self.__year_of_build
    def set_year_of_build(self, yb):
        self.__year_of_build = yb
    def get_plate_number(self):
        return self.__plate_number
    def get_vin_number(self):
        return self.__vin_number

honda_crv=Vehicle('Honda-crv',4,40000,2022)
hyundai_Elantra=Vehicle('Hyundai-Elanta',4,21000,2021)

# call instance methods for both cars
hyundai_Elantra.show_vehicle_info()
honda_crv.show_vehicle_info()
plate_nu_honda=honda_crv.get_plate_number()
plate_nu_hyundai=hyundai_Elantra.get_plate_number()
print('Honda plate number is : ',plate_nu_honda)
print('Hyndai plate number is : ',plate_nu_hyundai)

print('************ check VIN number of each car **')
print('**** if you call honda_crv.__vin_number then it raises Attribute error')
# print(honda_crv.__vin_number)
print(honda_crv.get_vin_number())
print(hyundai_Elantra.get_vin_number())

# call class methos.
Vehicle.show_total_vehicles()
