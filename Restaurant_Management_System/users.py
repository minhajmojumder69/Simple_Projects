from abc import ABC
from order import Order
class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

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

    def view_items(self,restaurant):
        restaurant.menu.show_menu()

    def delete_item(self,restaurant,item):
        restaurant.menu.remove_item(item)

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self,restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self,restautant,item_name,quantity):
        item = restautant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print('Item quantity exceeded..!!')
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print('Item added')
        else:
            print('Item not found')

    def view_cart(self):
        print('--- View Cart ---')
        print('Name\tPrice\tQuantity')
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price : {self.cart.total_price}")
    def pay_bill(self):
        tk = self.cart.total_price
        print(f'Total {tk}.')
        bill = int(input('Pay now : '))
        if bill < tk:
            more = tk - bill
            print(f"You have to pay more {more} tk.")
            self.cart.clear()
        elif tk < bill:
            extra = bill - tk
            print(f'Thanks for {extra} tk tips')
            self.cart.clear()
        else:
            print('Thank You..!!')
            self.cart.clear()

class Employee(User):
    def __init__(self, name, phone, email, address,age,disegnation,salary):
        self.age = age
        self.disegnation = disegnation
        self.salary = salary
        super().__init__(name, phone, email, address)