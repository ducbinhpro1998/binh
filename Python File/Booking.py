
class Booking:
    def __init__(self, customer, destination, quantity):
        self.customer = customer
        self.destination = destination
        self.quantity = quantity

    def get_customer(self):
        return self.customer

    def set_customer(self, customer):
        self.customer = customer

    def get_destination(self):
        return self.destination

    def set_destination(self, destination):
        self.destination = destination

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
