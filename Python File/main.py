from Record import * 
from Booking import *

fileCustomerName = "../Assignment/Source/customer.txt"
fileDestinationName = "../Assignment/Source/destinations.txt"
record = Record()
customers = record.read_customer_file(fileCustomerName)
destinations = record.read_destinations_file(fileDestinationName)

customerID = []
if customers != None:
    for i in range (len(customers)):
        customerID.append(customers[i].id)

def menu():
    print("-----------------------------MENU--------------------------")
    print("---------------      1. Book a new trip          ----------")
    print("---------------      2. List all Customer        ----------")
    print("---------------      3. List all destination     ----------")
    print("---------------      4. Exit program             ----------")

def addNewBook(customer, destination, quantity):
    if(customer.id not in customerID) :
        YNChoice = input("Want to be member? y /n :")
        if(YNChoice.lower() == "y"):
            memberChoice = input("Want to be? \n1.Member\n2.Vip Member")
            if(memberChoice == "1"):
                customer = Member(customer.id, customer.name, customer.value, 0.05)
                customer.value = float(customer.value) + float(destination.price) - customer.get_discount(destination.price)
                record.writeNewCustomer(customer, fileCustomerName)
                customers.append(customer)

            else:
                customer = VIPMember(customer.id, customer.name, customer.value, 0.1)
                customer.value = float(customer.value) + float(destination.price) - customer.get_discount(destination.price) + 100
                record.writeNewCustomer(customer, fileCustomerName)
                customers.append(customer)

        else:
            customer.value = float(customer.value) + float(destination.price)
            record.writeNewCustomer(customer, fileCustomerName)
            for cus in customers:
                if cus.id == customer.id:
                    customers.remove(cus)
                    print("delete success")
                    customers.append(customer)
    
    else:
        customer.value = float(customer.value) + float(destination.price) - customer.get_discount(destination.price)
        record.updateCustomerInFile(customer, fileCustomerName)


    destination.seatAvaiable = int(destination.seatAvaiable) - 1
    quantity = int(quantity) + 1
    booking = Booking(customer, destination, quantity)
    
    return booking

try:
    f = open(fileCustomerName, 'rb')
    ff = open(fileDestinationName, 'rb')
    while True :
        menu()
        choice = input("Input choice : ")
        if(choice == "1"):
            customer = None
            destination = None
            print("---------------------Create new Booking!!!-----------------------")
            id = input("Input Id Customer : ")
            if id not in customerID:
                name = input("You are new Customer\nInput Name : ")
                customer = Customer(id, name, 0)
            else :
                print("Welcome back " + id + " customer")
                for cus in customers:
                    if cus.id == id:
                        customer = cus
            
            print("Where you want to go: ")
            i = 1
            for des in destinations:
                print(f"{i}. {des.id}, {des.name}")
                i = i + 1
            
            desChoice = input("Input Id of Destination : ")
            for des in destinations:
                if des.id == desChoice:
                    destination = des

            #print(destination.price)
            addNewBook(customer, destination, 10)
            break
            
        if(choice == "2"):
            
except FileNotFoundError:
    print("File not founded!!!")
except IOError:
    print("IOE error file ")
finally:
    ff.close()
    f.close()
                    








    











