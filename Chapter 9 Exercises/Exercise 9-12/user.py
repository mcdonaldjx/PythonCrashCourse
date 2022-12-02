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
