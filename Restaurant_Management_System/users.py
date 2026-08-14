from abc import ABC
class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = None

    def view_menu(self,restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self,restautant,item_name):
        item = restautant.menu.find_item(item_name)
        if item:
            pass
        else:
            print('Item not found')

    def view_cart(self):
        print('--- View Cart ---')
        print('Name\tPrice\tQuantity')
        

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
        # self.employee_list = []   # as Database

    def add_employee(self,restaurant,employee):
        restaurant.add_employee(employee)
        
    def view_employee(self,restaurant):
        restaurant.view_employee()

    def add_new_item(self,restaurant,item):
        restaurant.menu.add_food(item)

    def delete_item(self,restaurant,item):
        restaurant.menu.remove_item(item)

# ad = Admin('Minhaj',12345676,'edu@gmail.com','Dhaka')
# ad.add_employee('Rakin',984829,'rakin@gmail.com','Sonir akhra',22,'Chef',22000)
# ad.add_employee('Sakira',9823829,'sakira@gmail.com','Sonir akhra',21,'Dancer',25000)
# ad.view_employee()

class Restaurant():
    def __init__(self,name):
        self.name = name
        self.employee_list = []   # as Database
        self.menu = FoodItem()

    def add_employee(self,employee):
            self.employee_list.append(employee)    # stored in database

    def view_employee(self):
            print('--- Employee List ---')
            for emp in self.employee_list:
                print(emp.name, emp.phone, emp.email, emp.address)

class Food_Menu:
    def __init__(self):
        self.item_list = []  # item database

    def add_food(self,item):
        self.item_list.append(item)

    def find_item(self,item_name):
        for item in self.item_list:
            if item.name.lower() == item_name.lower():
                return item
        return None
    
    def remove_item(self,item_name):
        item = self.find_item(item_name)
        if item:
            self.item_list.remove(item)
            print('Item deleted')
        else:
            print('Item not found')

    def show_menu(self):
        print('---- Menu ----')
        print('Name\tPrice\tQuantity')
        for item in self.item_list:
            print(f'{item.name}\t{item.price}\t{item.quantity}')
            
class FoodItem:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

mn = Food_Menu()
item = FoodItem('Pizza',299,20)
mn.add_food(item)
mn.show_menu()