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


class ShiftSupervisor(Employee):
    def __init__(self, name="", employee_number="", annual_salary=0.0, annual_bonus=0.0):
   
        super().__init__(name, employee_number)
        self.__annual_salary = annual_salary
        self.__annual_bonus = annual_bonus

    def get_annual_salary(self):
        return self.__annual_salary

    def get_annual_bonus(self):
        return self.__annual_bonus

    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary

    def set_annual_bonus(self, annual_bonus):
        self.__annual_bonus = annual_bonus



if __name__ == "__main__":
    print("Enter details for a Shift Supervisor:")

    name = input("Enter the supervisor's name: ")
    employee_number = input("Enter the supervisor's employee number: ")
    annual_salary = float(input("Enter the annual salary: "))
    annual_bonus = float(input("Enter the annual production bonus: "))

    supervisor = ShiftSupervisor()
    supervisor.set_name(name)
    supervisor.set_employee_number(employee_number)
    supervisor.set_annual_salary(annual_salary)
    supervisor.set_annual_bonus(annual_bonus)

    print("\nShift Supervisor Details:")
    print(f"Name: {supervisor.get_name()}")
    print(f"Employee Number: {supervisor.get_employee_number()}")
    print(f"Annual Salary: ${supervisor.get_annual_salary():,.2f}")
    print(f"Annual Production Bonus: ${supervisor.get_annual_bonus():,.2f}")