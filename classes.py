

class Student:
    first_name = "Ghosted"
    last_name = "Gustanzo"
    gender = "Male"
    age = 18

class Person:
    def __init__(self, name, gender, marital_status, occupation):
        self.name = name
        self.gender = gender
        self.marital_status = marital_status
        self.occupation = occupation

    def salute(self):
        print(f'Good morning, {self.name}. You are  {self.marital_status}.')
    def display_name(self):
        print(f'You are {self.name} of gender  {self.gender}.')


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def perimeter(self):
        print(f'perimeter is {2 * (self.width + self.height)} metres.')
    def area(self):
       print(f'area is {self.width * self.height}square metres.')
    def display(self):
        print(f'{self.width} and {self.height}')

class My_Employee():
    def __init__(self,name, gender, basic_salary ,age):
        self.name = name
        self.gender = gender
        self.basic_salary = basic_salary
        self.age = age
    def my_salary(self):
        my_salary = self.basic_salary + 41500
        return my_salary
class Developer(My_Employee):
    def __init__(self,name,gender,basic_salary,age, prog_lang):
        super().__init__(name, gender, basic_salary, age)
        self.prog_lang = prog_lang
class Teacher(My_Employee):
    def __init__(self,name,gender,basic_salary,age, subject, xp_yrs):
        super().__init__(name, gender, basic_salary, age)
        self.subject = subject
        self.xp_yrs = xp_yrs
    def increment(self):
        increment = self.basic_salary + 10000
        return increment
class Hourly_Employee(My_Employee):
    def __init__(self,name,gender,basic_salary,age, hourly_rate, hours_worked):
        super().__init__(name, gender, basic_salary, age)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def hourly_employee_salary(self):
        hourly_employee_salary = self.basic_salary + (self.hourly_rate * self.hours_worked)
        return hourly_employee_salary

class BankAccount():
    def __init__(self,name, gender, IDNo, balance, deposits):
        self.name = name
        self.gender = gender
        self.IDNo = IDNo
        self.balance = balance
        self.deposits = deposits
    def deposit(self):
            print(f'You have deposited  {self.deposits}.')
class Transactions(BankAccount):
    def __init__(self,name,gender,IDNo,balance, deposits, amt_withdrawn):
        super().__init__(name, gender, IDNo, balance, deposits)
        self.amt_withdrawn = amt_withdrawn
    def withdraw(self):
        if self.amt_withdrawn == 0 or self.amt_withdrawn < self.balance:
            print(f'You are unable to withdraw since tour account balance is zero.')
        else:
            print(f'You have successfully withdrawn {self.amt_withdrawn}.')
    def bank_fee(self):
        print(f'You have been charged a bank fee of {0.05 * self.balance}.')
    def acc_details(self):
        print({self.name, self.gender, self.IDNo,self.deposits,self.bank_fee,self.balance})


