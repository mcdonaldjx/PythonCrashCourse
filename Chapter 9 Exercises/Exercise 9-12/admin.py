from user import User
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
