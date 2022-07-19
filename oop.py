import csv
from csv import DictReader
class Item:
    pay_rate = 0.8 # this is the class attribute
    all = [] # a list which contains all the instances
    def __init__(self, name: str, price: float, quantity): #This is putted at the begiin of a class to initialize every instances that pass through the class(check whether that instance has all the required info to properly be an instance)
        # Run validations to the received
        assert price >= 0, f"Price {price} is not greater than 0"  # this is a kind of statement which checks whether happening things
        assert quantity >= 0, f"The quantity {quantity} is not greater than 0" # meet the expectations that we set

        # Assign self object
        self.name = name 
        self.price = price
        self.quantity = quantity

        # Adding every add instance into the list all = []
        Item.all.append(self) #because all is a list so we could use append()
    
    def calculate_total_price(self): #a method is a function inside a class. The self arg because there always be parameters that you use and python try to pass that in the class
        # return x * y: you don't need to add any para like x and y because having filtered from the initializer, each instance has all the info for using
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate# you can use Item.pay_rate for Class level. But the best practice is self.pay_rate( at the Instance level) so that you can easily specify exemption for any other instance
        return(self.price)

    @classmethod # the decorator that convert a method into a class method. It will change the behavior of this method
    def instantiate_from_csv(cls): # when we call a cls med, the object itself will be the first arg to be passed into this med
        with open ('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    def __repr__(self): #This is a magic method used for representing the objects occuring in the console
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

class Phone(Item):
    #all = []
    # When we add a __init__ into a child class, we have to add the super function too. It allows us to have full access to all atts/meds(both at the class or instance level) of the parents class => fully implement the parents class, don't need to hard code the assertions or object assignments
    def __init__(self, name: str, price: float, quantity, broken_phones=0): #This is putted at the begiin of a class to initialize every instances that pass through the class(check whether that instance has all the required info to properly be an instance)
        super().__init__(
            name, price, quantity
        )
        # Run validations to the received
        #assert price >= 0, f"Price {price} is not greater than or equals to 0"  # this is a kind of statement which checks whether happening things
        #assert quantity >= 0, f"The quantity {quantity} is not greater than or equals to 0" # meet the expectations that we set
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equals to 0"

        # Assign self object
        # self.name = name 
        # self.price = price
        # self.quantity = quantity
        self.broken_phones = broken_phones

        # Adding every add instance into the list all = []
        #Phone.all.append(self) #because all is a list so we could use append()

phone1 = Phone("Iphone13", 100, 5, 1) # we have Phone is the inheritance of Item, but it has one more attr which is broken_phones so we have to pass it through the Phone class(then add broken_phones attr to this class) rather than pass it to the Item class
print(phone1.calculate_total_price())
#phone1.broken_phones = 1
phone2 = Phone("Iphone8", 1000, 5, 1)
#phone2.broken_phones = 1

print(Item.all)
print(Phone.all)