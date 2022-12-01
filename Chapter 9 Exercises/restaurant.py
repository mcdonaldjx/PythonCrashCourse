#Created 11/30/2022 by Jared
#Exercise 9-1- Restaurant: Make a class called Restaurant. The __int__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
#   Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"This restaurant is named {self.restaurant_name.title()}")
        print(f"This restaurant serves {self.cuisine_type.title()} food")
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!")
        
my_restaurant = Restaurant('margaritas', 'mexican')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
