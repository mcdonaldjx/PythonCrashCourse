#Created 12/1/2022 by Jared
#Exercise 9-6- Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 or 9-4. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type.title()} cuisine")
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!")
        
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.flavors = ['vanilla','cookies & cream', 'chocolate chip cookie dough']
    def display_flavors(self):
        print(f"{self.restaurant_name.title()} has these flavors:")
        for flavor in self.flavors:
            print(f"\t{flavor.title()}")
            
ice_cream_stand = IceCreamStand('hanks ice cream', 'ice cream')
ice_cream_stand.display_flavors()
