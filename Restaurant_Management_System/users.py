from abc import ABC
class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Employee(User):
    def __init__(self, name, phone, email, address,age,disegnation,salary):
        self.age = age
        self.disegnation = disegnation
        self.salary = salary
        super().__init__(name, phone, email, address)

# emp = Employee('Sadia Afrin',123456,'sdi@gmail.com','Gulsan',22,'Chef',20000)
# print(emp.name)

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.employee_list = []   # as Database

    def add_employee(self,name,phone,email,address,age,disegnation,salary):
        employee = Employee(name,phone,email,address,age,disegnation,salary)
        self.employee_list.append(employee)    # stored in database
        print(f'{name} added!')

    def view_employee(self):
        print('--- Employee List ---')
        for emp in self.employee_list:
            print(emp.name, emp.phone, emp.email, emp.address)

ad = Admin('Minhaj',12345676,'edu@gmail.com','Dhaka')
ad.add_employee('Rakin',984829,'rakin@gmail.com','Sonir akhra',22,'Chef',22000)
ad.add_employee('Sakira',9823829,'sakira@gmail.com','Sonir akhra',21,'Dancer',25000)
ad.view_employee()