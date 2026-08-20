from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self,name,email,nid):
        self.name = name
        self.email = email
        self.nid = nid
        self.wallet = 0
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError

class Rider(User):
    def __init__(self, name, email, nid,location,initial_amount):
        super().__init__(name, email, nid)
        self.location = location
        self.wallet = initial_amount
        self.current_ride = None

    def display_profile(self):
        print(f'Rider Name : {self.name}, Email : {self.email}')
    def load_cash(self,amount):
        if amount > 9:
            self.wallet += amount
        else:
            print("Minimun recharge 10 tk")
    def update_location(self,currect_location):
        self.location = currect_location
