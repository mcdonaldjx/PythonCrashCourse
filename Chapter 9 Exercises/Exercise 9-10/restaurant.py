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
