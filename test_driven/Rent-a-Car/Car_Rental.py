from dataclasses import dataclass


@dataclass
# class Car_Renterer:
#     def __init__(self, name_of_renter): 
#         self.name = name_of_renter
        
#     def set_renterer_details(self, name):
#         self.name = name
    
#     def get_renterer_details(self):
#         return self.name

    
@dataclass
class CarRental:
    def __init__(self, company_name):
        self.company_name = company_name
        self.premium_car_daily_rate = 100
        self.non_premium_car_daily_rate = 40.0
        self.insurance_per_day = 30
        self.netCost = 0.0
    
    def Rent_a_car(self, number_of_days, premium_car):
        if premium_car:
            self.netCost = (self.premium_car_daily_rate + self.insurance_per_day) * number_of_days
        else:
             self.netCost = (self.non_premium_car_daily_rate + self.insurance_per_day) * number_of_days
        
    def Rental_cost(self) -> float:
        return self.netCost

