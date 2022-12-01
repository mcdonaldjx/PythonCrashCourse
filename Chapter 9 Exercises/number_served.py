#Created 12/1/2022 by Jared
#Exercise 9-4- Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the resaurant has served, and then change this value and print it again.
#   Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again.
#   Add a method called increment_number_served() that lets you increment the number of customers who've been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business.
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe a restaurant."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
    def set_number_served(self, served):
        self.number_served = served
    def increment_number_served(self, served_count):
        self.number_served += served_count
my_restaurant = Restaurant('margaritas', 'mexican')
my_restaurant.set_number_served(0)
print(f"So far {my_restaurant.restaurant_name} has served {my_restaurant.number_served} customers.")
my_restaurant.increment_number_served(60)
print(f"{my_restaurant.restaurant_name} has served {my_restaurant.number_served} customers today.")
