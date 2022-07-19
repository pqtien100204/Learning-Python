from oop_item import Item

class Phone(Item):

    def __init__(self, name: str, price: float, quantity, broken_phones=0): #This is putted at the begiin of a class to initialize every instances that pass through the class(check whether that instance has all the required info to properly be an instance)
        super().__init__(
            name, price, quantity
        )
        # Run validations to the received
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equals to 0"

        # Assign self object
        self.broken_phones = broken_phones

