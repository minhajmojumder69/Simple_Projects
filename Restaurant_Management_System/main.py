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
            customer.view_menu(dadur_dokan)
        elif choice == 2:
            item_name = input('Enter food name : ')
            item_quantity = input('Enter food quantity : ')
            customer.add_to_cart(dadur_dokan,item_name,item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            print(f'Thank You {customer.name}')
            break
        else:
            print('Invalid choice !')


def admin_menu():
    name = input('Enter your name : ')
    email = input('Enter your email : ')
    phone = input('Enter your phone number : ')
    address = input('Enter your address : ')

    admin = Admin(name=name,email=email,phone=phone,address=address)

    while True:
        print(f'Welcome {admin.name} !!')
        print('1. Add New Item')
        print('2. Add New Employee')
        print('3. View Employee')
        print('4. View Items')
        print('5. Delete Items')
        print('6. Exit')

        choice = int(input('Enter your choice (1-5) : '))
        if choice == 1:
            item_name = input('Enter item name : ')
            item_price = int(input('Enter item price : '))
            item_quantity = int(input('Enter item quantity :'))
            item = FoodItem(item_name,item_price,item_quantity)
            admin.add_new_item(dadur_dokan,item)

        elif choice == 2:
            emp_name = input('Employee Name : ')
            emp_phone = input('Phone : ')
            emp_email = input('Email : ')
            emp_address = input('Address : ')
            emp_age = int(input('Age : '))
            emp_disegnation = input('disegnation : ')
            emp_salary = int(input('Salary : '))
            employee = Employee(emp_name,emp_phone,emp_email,emp_address,emp_age,emp_disegnation,emp_salary)
            admin.add_employee(dadur_dokan,employee)

        elif choice == 3:
            admin.view_employee(dadur_dokan)

        elif choice == 4:
            admin.view_items(dadur_dokan)

        elif choice == 5:
            item = input('Enter item name : ')
            admin.delete_item(dadur_dokan,item)

        elif choice == 6:
            print(f'Thank You {admin.name}')
            break
        else:
            print('Invalid choice !')

def login():
    print('#********************************#')
    print(f'----- Welcome to {dadur_dokan.name} -----')
    print('#********************************#')
    while True:
        print(f'Log in as Admin/Customer...')
        print('1. Admin')
        print('2. Customer')
        print('3. Exit')
        choice = int(input('Enter your choice : '))
        if choice == 1:
            admin_menu()
        elif choice == 2:
            customer_menu()
        elif choice == 3:
            break
        else:
            print('Invalid choice')
login()