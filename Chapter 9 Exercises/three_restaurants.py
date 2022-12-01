#Created 11/30/2022 by Jared
#Exercise 9-2- Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and describe_restaurant() for each instance.
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type.title()} cuisine")
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!")
        
first_restaurant = Restaurant('margaritas', 'mexican')
first_restaurant.describe_restaurant()
first_restaurant = Restaurant('north italia', 'italian')
first_restaurant.describe_restaurant()
first_restaurant = Restaurant('pappasitos', 'seafood')
first_restaurant.describe_restaurant()
