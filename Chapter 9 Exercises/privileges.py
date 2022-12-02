#Created 12/1/2022 by Jared
#Exercise 9-8- Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges. 
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
        
class Privileges():
    def __init__(self):
        self.list_of_privileges = ['can add post', 'can delete post', 'can ban user', 'can add user']
    def show_privileges(self):
        print(f"List of Privileges:")
        for privilege in self.list_of_privileges:
            print(f"\t{privilege}")
        
class Admin(User):
    def __init__(self, first_name, last_name, **attributes):
        self.first_name = first_name
        self.last_name = last_name
        self.attributes = attributes
        self.privileges = Privileges()
        
user_a = Admin('jared','m', age=29, country='united states')
user_a.privileges.show_privileges()
