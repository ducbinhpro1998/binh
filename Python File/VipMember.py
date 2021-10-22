from Customer import *

threshold = 1000
class VIPMember(Customer):
    def __init__(self, id, name, value,rate_discount):
        super().__init__(id, name, value)
        self.rate_discount = float(rate_discount)
        self.second_rate_discount = float(rate_discount) + 0.05
    
    def get_discount(self, cost):
        if float(cost) <= float(threshold):
            discount_rate_booking = float(cost) * self.rate_discount
        else:
            discount_rate_booking = float(cost) * self.second_rate_discount

        return discount_rate_booking
    def setThreshold(self, new_threshold):
        global threshold
        threshold = new_threshold

    def displayCustomer(self):
        print(f"Id= {self.id}, name = {self.name}, price = {self.value}, first discount = {self.rate_discount}, second discount = {self.second_rate_discount}")
