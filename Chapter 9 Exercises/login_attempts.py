#Created 12/1/2022 by Jared
#Exercise 9-5- Login Attempts: Add an attribute called login_attemps to your User class from Exercise 9-3. Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
#   Make an instance of the User class and call increment_login_attempts() several times. Prit the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
class User:
    def __init__(self, first_name, last_name, **attributes):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} has {self.login_attempts} login attempts")
    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
first_user = User('john', 'doe')
first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.describe_user()
first_user.reset_login_attempts()
first_user.describe_user()
