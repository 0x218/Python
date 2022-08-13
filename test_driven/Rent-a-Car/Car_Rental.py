from dataclasses import dataclass
    
@dataclass
class CarRental:
    # def __init__(self, company_name):
    #     self.company_name = company_name
    #     self.premium_car_daily_rate = 100
    #     self.non_premium_car_daily_rate = 40.0
    #     self.insurance_per_day = 30
    #     self.net_cost = 0.0
    #
    #
    # # magic function to return class object
    # def __repr__(self):
    #     return ("CarRental (company_name={}, premium_car_daily_rate={}, non_premium_car_daily_rate={}, insurance_per_day={},netCost={} )"
    #             .format(self.company_name, self.premium_car_daily_rate, self.non_premium_car_daily_rate, self.insurance_per_day,self.net_cost,))
    #
    #
    # # magic function to return boolean
    # def __eq__(self, cmpObj):
    #     return ((self.company_name, self.premium_car_daily_rate, self.non_premium_car_daily_rate, self.insurance_per_day, self.net_cost,) ==
    #          (cmpObj.company_name, cmpObj.premium_car_daily_rate, cmpObj.non_premium_car_daily_rate, cmpObj.insurance_per_day,cmpObj.net_cost))
    #
    #


    ## dataclasses automatially includes __init__(), __repr__() and __eq__().
    ## No need for the __init__, but uninitialized variables become mandatory arguments (here it is company_name).

      
    company_name: str ##uninitialized variables should be declared first
    premium_car_daily_rate : float = 100
    non_premium_car_daily_rate : float = 40.0
    insurance_per_day : int = 30
    net_cost : float = 0.0

    def Rent_a_car(self, number_of_days, premium_car):
        if premium_car:
            self.net_cost = (self.premium_car_daily_rate + self.insurance_per_day) * number_of_days
        else:
             self.net_cost = (self.non_premium_car_daily_rate + self.insurance_per_day) * number_of_days
        
    def Rental_cost(self) -> float:
        return self.net_cost



