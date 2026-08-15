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
        self.cart = Order()

    def view_menu(self,restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self,restautant,item_name,quantity):
        item = restautant.menu.find_item(item_name)
        if item:
            item.quantity = quantity
            self.cart.add_item(item)
            print('Item added')
        else:
            print('Item not found')

    def view_cart(self):
        print('--- View Cart ---')
        print('Name\tPrice\tQuantity')
        for item,quantity in self.cart.items.items():
            print(f"{item.name} {item.price} {quantity}")
        print("Total Price : {self.cart.total_price}")

class Order:
    def __init__(self):
        self.items = {} 

    def add_item(self,item):
        if item in self.items:
            self.items[item] += item.quantity
        else:
            self.items[item] = item.quantity

    def remove(self,item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(item.price * quantity for item,quantity in self.items.items())
    def clear(self):
        self.items = {}

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
        self.menu = Food_Menu()

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


dadur_dokan = Restaurant('Dadur Dokan')
ad = Admin('Minhaj',12345676,'edu@gmail.com','Dhaka')

item = FoodItem('Pizza',299,20)
item2 = FoodItem('Burger',269,9)
ad.add_new_item(dadur_dokan,item)
ad.add_new_item(dadur_dokan,item2)

# mn = Food_Menu()
# item = FoodItem('Pizza',299,20)
# item2 = FoodItem('Burger',269,9)
# mn.add_food(item)
# mn.add_food(item2)
#mn.show_menu()

costomer1 = Customer('Mahin',93848,'mahi@gmail.com','Dhaka')
costomer1.view_menu(dadur_dokan)
costomer1.add_to_cart(dadur_dokan,'pizza',2)
costomer1.view_cart()