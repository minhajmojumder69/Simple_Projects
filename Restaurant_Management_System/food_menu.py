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