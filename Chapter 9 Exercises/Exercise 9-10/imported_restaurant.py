#Created 12/2/2022 by Jared
#Exercise 9-10- Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. Make a Restaurant instance, and call one of Restaurant's methods to show that the import statement is working properly.
import restaurant as res
favorite_restaurant = res.Restaurant('bobs taco station','mexican')
favorite_restaurant.describe_restaurant()
