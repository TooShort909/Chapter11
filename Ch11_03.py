class Person:
    def __init__(self, name, address, telephone):

        self.__name = name
        self.__address = address
        self.__telephone = telephone


    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_telephone(self):
        return self.__telephone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_telephone(self, telephone):
        self.__telephone = telephone


class Customer(Person):
    def __init__(self, name, address, telephone, customer_number, mailing_list):

        Person.__init__(self, name, address, telephone)
        self.__customer_number = customer_number
        self.__mailing_list = mailing_list

    def set_customer_number(self, customer_number):
        self.__customer_number = customer_number

    def set_mailing_list(self, mailing_list):
        self.__mailing_list = mailing_list
  
    def get_customer_number(self):
        return self.__customer_number

    def get_mailing_list(self):
        return self.__mailing_list


if __name__ == "__main__":
    print("Enter details for a Customer:")

    name = input("Enter the customer's name: ")
    address = input("Enter the customer's address: ")
    telephone = input("Enter the customer's telephone number: ")
    customer_number = int(input("Enter the customer number: "))
    mail = input("Is the customer on the mailing list? (y/n): ")

    if mail.lower() == 'y':
        mailing_list = True
    else:
        mailing_list = False

    my_customer = Customer(name, address, telephone, customer_number, mailing_list)

    print("\nCustomer Details:")
    print('Name:', my_customer.get_name())
    print('Address:', my_customer.get_address())
    print('Telephone:', my_customer.get_telephone())
    print('Customer Number:', my_customer.get_customer_number())
    print('On Mailing List:', my_customer.get_mailing_list())