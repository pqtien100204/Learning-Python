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
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


item1 = Item("Phone", 100, 1) #This is an instance of the class
print(item1.apply_discount())   #OR   #item1.apply_discount()
#item1.name = "Phone"                 #print(item1.price)
#item1.price = 100                                                                  don't have to hard code every instance
#item1.quantity = 5                                                                  with the help of the __init_
print(item1.calculate_total_price(item1.price, item1.quantity)) #calling a method

item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7 # you can directly set a new value(of the class attribute) for a single specific instance(set attribute in the instance level).
item2.apply_discount()
print(item2.price) 

print(Item.__dict__) #this give all the attribute for the Class level
print(item1.__dict__) # this give all the attribute for the Instance level
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

Item.instantiate_from_csv() # A class method instantiate_from_csv() can only be accessed by the class level(Item). It works with the whole object(Item), not the instance of that object
print(Item.all) #this would show with every instance being add to the class, it will be added to the all list as well. We could use for loop to see things clearer
# for instance in Item.all:
#     print(instance.name)
print(Item.is_integer(8.9))

