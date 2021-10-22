from Customer import *
from Member import *
from VipMember import *
from Destination import *

class Record:
    def __init__(self) -> None:
        pass

    def read_customer_file(self, fileCustomerName):
        objects = []
        object = None
        with open(fileCustomerName) as f:
            lines = f.readlines()
            for k in range (len(lines)):
                line = lines[k].rstrip().split(', ')
                
                if(line[0].startswith("C")):
                    object = Customer(line[0], line[1], line[3])

                if(line[0].startswith("M")):
                    object = Member(line[0], line[1], line[3], float(line[2]))

                if(line[0].startswith("V")):
                    object = VIPMember(line[0], line[1], line[3], float(line[2]))

                objects.append(object)
        return objects
    
    def read_destinations_file(self, fileDestinationName):
        objects = []
        object = None
        with open(fileDestinationName) as f:
            lines = f.readlines()
            for k in range (len(lines)):
                line = lines[k].rstrip().split(', ')
                
                if(line[0].startswith("D")):
                    object = Destination(line[0], line[1], line[2], line[3])
                objects.append(object)
        return objects

    def findCustomer(self, customer_id):
        for object in self.read_customer_file():
            if object.id == customer_id:
                return object
        return None

    def findDestination(self, destination_id):
        for object in self.read_destinations_file():
            if object.id == destination_id:
                return object
        return None

    def listCustomer(self):
        for object in self.read_customer_file() :
            object.displayCustomer()

    def listDestination(self) :
        for object in self.read_destinations_file() :
            object.displayDestination()

    def writeNewCustomer(self, customer, fileCustomerName):
        try:
            file = open(fileCustomerName, 'a')
            file.writelines(f"\n{customer.id}, {customer.name}, {customer.rate_discount}, {customer.value}")
        except IOError:
            print("IOE error")
        except FileNotFoundError:
            print("File not found")
        finally:
            file.close()

    def updateCustomerInFile(self, customer, fileCustomerName):
        try:
            file = open(fileCustomerName, "r")
            lines = file.readlines()
            file.close()

            for i in range (len(lines) - 1):
                if lines[i].startswith(customer.id) :
                    del lines[i]
            
            new_file = open(fileCustomerName, "w+")
            for line in lines:
                new_file.write(line)
            new_file.close()
            self.writeNewCustomer(customer, fileCustomerName)
        except IOError:
            print("IOE error")
        except FileNotFoundError:
            print("File not found")
        finally:
            file.close()
