# all imports are done at the top
from classes import Student, Person, Vehicle, Rectangle, My_Employee, Developer, Teacher, Hourly_Employee, BankAccount,Transactions

student1 = Student()
print(student1.first_name)
print(student1.last_name)
print(student1.age)
print(student1.gender)


person1 = Person("Ghost", "Male", "Married", "Plumber")
person2 = Person("Anne", "Female", "Divorced", "Chef")
person3 = Person("Bobby", "Male", "Single", "Engineer")
print(person1.marital_status)
print(person2.gender)
print(person3.name)
person1.salute()
person2.salute()
person3.salute()
person1.display_name()
person2.display_name()
person3.display_name()




vehicle1 = Vehicle("Toyota", "Supra", "1997")
vehicle2 = Vehicle("Ford", "Mustang", "1964")
vehicle3 = Vehicle("Volkswagen", "Beetle", "1934")
print(vehicle1.make)
print(vehicle2.model)
print(vehicle3.year)

rectangle1 = Rectangle(100, 80)
rectangle1.perimeter()
rectangle1.area()
rectangle1.display()

my_employee1 = My_Employee("Ghost", "Male", 150000, 21)
my_employee2 = My_Employee("Charly", "Female", 100000, 24)
print(my_employee1.basic_salary)
print(my_employee2.gender)
print(my_employee1.my_salary())
print(my_employee2.my_salary())

developer1 = Developer("Ghost", "Male", 240000, 21, "Kotlin")
developer2 = Developer("Charly", "Female", 100000, 24, "Python")
print(developer1.my_salary())

teacher1 = Teacher("Ghost", "Male", 240000, 21, "Modern Warfare", 5)
teacher2 = Teacher("Charly", "Female", 100000, 24, "Black Ops", 4)
print(teacher1.increment())
print(teacher2.increment())

hourly_emp1 = Hourly_Employee("Ghost", "Male", 240000, 21, 1000, 12)
hourly_emp2 = Hourly_Employee("Charly", "Female", 100000, 24, 700, 9)
print(hourly_emp1.hourly_employee_salary())
print(hourly_emp2.hourly_employee_salary())

client1 = Transactions("Ghost", "Male", 12345, 21000, 56876, 354 )
print(client1.acc_details())