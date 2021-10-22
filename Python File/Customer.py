class Customer:
    def __init__(self, id, name, value=0):
        self.id = id
        self.name = name
        self.value = value
        self.rate_discount = 0

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_totalMoney(self):
        return self.value

    def set_id(self, id):
        self.id = id

    def set_id(self, name):
        self.name = name

    def set_id(self, value):
        self.value = value    
    
    def get_discount(self, cost):
        return 0

    def displayCustomer(self):
        print(f"Id = {self.id}, name = {self.name}, price = {self.value}")