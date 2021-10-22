from Customer import *

class Member(Customer):
    def __init__(self, id, name, value, rate_discount=0.05):
        super().__init__(id, name, value)
        self.rate_discount = rate_discount
    
    def get_discount(self, cost):
        discount_rate_booking = float(cost)*self.rate_discount
        return discount_rate_booking
    
    def setRate(self, rate_discount):
        self.rate_discount = rate_discount

    def displayCustomer(self):
        print(f"Id = {self.id}, name = {self.name}, price = {self.value}, discount = {self.rate_discount}")