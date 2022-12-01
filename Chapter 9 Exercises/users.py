#Created 11/30/2022 by Jared
#Exercise 9-3- Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user's information. Make another method called greet_user() that prints a personalized greeting to the user.
    #Create several instances representing different users, and call both methods for each user.
class User:
    def __init__(self, first_name, last_name, **attributes):
        self.first_name = first_name
        self.last_name = last_name
        self.attributes = attributes
    def describe_user(self):
        print(f"Information on {self.first_name.title()} {self.last_name.title()}:")
        for a in self.attributes:
            print(f"\t{a.title()}: {self.attributes[a]}")
    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")
first_user = User('john', 'doe', age=25, eye_color='brown', hair_color='black')
first_user.greet_user()
first_user.describe_user()
second_user = User('jane', 'doe', age=29, eye_color='brown', hair_color='red')
second_user.greet_user()
second_user.describe_user()
third_user = User('jared', 'm', age=29, eye_color='brown', hair_color='black')
third_user.greet_user()
third_user.describe_user()
