class Destination:
    def __init__(self, id, name, price, seatAvaiable):
        self.id = id
        self.name = name
        self.price = price
        self.seatAvaiable = seatAvaiable
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        self.price = new_price   
    
    def set_seatAvaiable(self, new_seatAvaiable):
        self.seatAvaiable = new_seatAvaiable

    def displayDestination(self) :
        print(f"Id = {self.id}, name = {self.name}, price = {self.price}, seatAvaiable = {self.seatAvaiable}")
