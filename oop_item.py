import csv

class Item:
    pay_rate = 0.8 # this is the class attribute
    all = [] # a list which contains all the instances
    def __init__(self, name: str, price: float, quantity): #This is putted at the begiin of a class to initialize every instances that pass through the class(check whether that instance has all the required info to properly be an instance)
        # Run validations to the received values
        assert price >= 0, f"Price {price} is not greater than 0"  # this is a kind of statement which checks whether happening things
        assert quantity >= 0, f"The quantity {quantity} is not greater than 0" # meet the expectations that we set

        # Assign self object
        self.__name = name 
        self.price = price
        self.quantity = quantity

        # Adding every add instance into the list all = []
        Item.all.append(self) #because all is a list so we could use append()
    
    @property
    def name(self):
        return self.__name

    @name.setter # this decorator helps to set a new value for the var which has the @property decorator
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    def calculate_total_price(self): #a method is a function inside a class. The self arg because there always be parameters that you use and python try to pass that in the class
        # return x * y: you don't need to add any para like x and y because having filtered from the initializer, each instance has all the info for using
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate# you can use Item.pay_rate for Class level. But the best practice is self.pay_rate( at the Instance level) so that you can easily specify exemption for any other instance
        return(self.price)

    @classmethod # the decorator that convert a method into a class method. It will change the behavior of this method
    def instantiate_from_csv(cls): # when we call a cls med, the object itself will be the first arg to be passed into this med
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    def __repr__(self): #This is a magic method used for representing the objects occuring in the console
        return f"{self.__class__.__name__}'{self.name}', {self.price}, {self.quantity})"

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # @property # this decorator helps to prevent making changes to varibles(the read-only mode)
    # def read_only_name(self):
    #     return "AAA"