#Created 12/1/2022 by Jared
#Exercise 9-7- Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you worte in Exercise 9-3 or 9-5. Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges() that lists the administrator's set of priviiges. Create an instance of Admin, and call your method. 
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

class Admin(User):
    def __init__(self, first_name, last_name, **attributes):
        self.first_name = first_name
        self.last_name = last_name
        self.attributes = attributes
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can add user']
    def show_privileges(self):
        print(f"Privileges of {self.first_name.title()} {self.last_name.title()}:")
        for privilege in self.privileges:
            print(f"\t{privilege}")
            
user_a = Admin('jared','m', age=29, country='united states')
user_a.show_privileges()
