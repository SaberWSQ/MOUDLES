"""
Program: overriding.py
Author: Shiqi Wang
Last date modified: 11/03/2020

The purpose of this program is to create employee class and 2 derived classes: SalariedEmployee, HourlyEmployee
"""
import datetime


class Employee:
    """Employee Class"""

    # constructor
    def __init__(self, lname, fname, address, phone_number):
        self.last_name = lname
        self.first_name = fname
        self.address = address
        self.phone_number = phone_number

    def display(self):
        """Return basic information about the employee
        :return: str
        """
        res = ""
        res += f"{self.last_name} {self.first_name}\n"
        res += f"address: {self.address}\n"
        res += f"phone number: {self.phone_number}"

        return res


class SalariedEmployee(Employee):
    def __init__(self, lname, fname, address, phone_number, start_date, salary):
        super().__init__(lname, fname, address, phone_number)
        self.start_date = start_date
        self.salary = salary

    def give_raise(self, new_salary):
        self.salary = new_salary

    def display(self):
        res = f"start date: {self.start_date}\nsalary: ${self.salary:,}"
        return super().display() + '\n' + res


class HourlyEmployee(Employee):
    def __init__(self, lname, fname, address, phone_number, start_date, hourly_pay):
        super().__init__(lname, fname, address, phone_number)
        self.start_date = start_date
        self.hourly_pay = hourly_pay

    def give_raise(self, new_hourly_pay):
        self.hourly_pay = new_hourly_pay

    def display(self):
        res = f"start date: {self.start_date}\nhourly pay: ${self.hourly_pay:.2f}"
        return super().display() + '\n' + res


if __name__ == '__main__':
    today = datetime.date.today().strftime("%m/%d/%y")
    employee_1 = SalariedEmployee("Wang", "Shiqi", "no address", "no phone", today, 40000)
    print(employee_1.display())
    employee_1.give_raise(45000)
    print(employee_1.display())
    del employee_1

    print("=" * 50)

    employee_2 = HourlyEmployee("Wang", "Shiqi", "no address", "no phone", today, 10.00)
    print(employee_2.display())
    employee_2.give_raise(12.00)
    print(employee_2.display())
    del employee_2
