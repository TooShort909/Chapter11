class Employee:
    def __init__(self, name="", employee_number=""):
     
        self.__name = name
        self.__employee_number = employee_number

    def get_name(self):
        return self.__name

    def get_employee_number(self):
        return self.__employee_number

    def set_name(self, name):
        self.__name = name

    def set_employee_number(self, employee_number):
        self.__employee_number = employee_number


class ProductionWorker(Employee):
    def __init__(self, name="", employee_number="", shift_number=1, hourly_pay_rate=0.0):
        """
        Initialize a ProductionWorker object.
        :param name: Employee's name
        :param employee_number: Employee's unique number
        :param shift_number: Shift number (1 for day, 2 for night)
        :param hourly_pay_rate: Hourly pay rate
        """
        super().__init__(name, employee_number)
        self.__shift_number = shift_number
        self.__hourly_pay_rate = hourly_pay_rate

    def get_shift_number(self):
        return self.__shift_number

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate

    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate


if __name__ == "__main__":
    print("Enter details for a Production Worker:")

    name = input("Enter the employee's name: ")
    employee_number = input("Enter the employee's number: ")
    shift_number = int(input("Enter the shift number (1 for day, 2 for night): "))
    hourly_pay_rate = float(input("Enter the hourly pay rate: "))

    worker = ProductionWorker()
    worker.set_name(name)
    worker.set_employee_number(employee_number)
    worker.set_shift_number(shift_number)
    worker.set_hourly_pay_rate(hourly_pay_rate)

    print("\nProduction Worker Details:")
    print(f"Name: {worker.get_name()}")
    print(f"Employee Number: {worker.get_employee_number()}")
    shift = "Day" if worker.get_shift_number() == 1 else "Night"
    print(f"Shift: {shift}")
    print(f"Hourly Pay Rate: ${worker.get_hourly_pay_rate():.2f}")
