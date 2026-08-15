from food_menu import Food_Menu

class Restaurant():
    def __init__(self,name):
        self.name = name
        self.employee_list = []   # as Database
        self.menu = Food_Menu()

    def add_employee(self,employee):
            self.employee_list.append(employee)    # stored in database

    def view_employee(self):
            print('--- Employee List ---')
            for emp in self.employee_list:
                print(emp.name, emp.phone, emp.email, emp.address)