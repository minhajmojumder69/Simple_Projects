from food_item import FoodItem
from food_menu import Food_Menu
from order import Order
from restaurant import Restaurant
from users import User,Admin, Employee, Customer

dadur_dokan = Restaurant('Dadur Dokan')

def customer_menu():
    name = input('Enter your name : ')
    email = input('Enter your email : ')
    phone = input('Enter your phone number : ')
    address = input('Enter your address : ')

    customer = Customer(name=name,email=email,phone=phone,address=address)

    while True:
        print(f'Welcome {customer.name} !!')
        print('1. View Menu')
        print('2. Add item to cart')
        print('3. View cart')
        print('4. Pay bill')
        print('5. Exit')

        choice = int(input('Enter your choice (1-5) : '))
        if choice == 1:
            customer.view_menu()
        elif choice == 2:
            item_name = input('Enter food name : ')
            item_quantity = input('Enter food quantity : ')
            customer.add_to_cart(dadur_dokan,item_name,item_quantity)
        elif choice == 3:
            customer.view_menu()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            print(f'Thank You {customer.name}')
            break
        else:
            print('Invalid choice !')