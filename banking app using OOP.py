# Banking System using OOP
# Parent Class : User
# Holds details about a user (Done)
# Has a function to show user details (Done)
# Child Class : Bank (Done)
# Stores details about the account balance (Done)
# Stores details about the amount  (Done)
# Allows for deposits, withdraw, view_balance

# Parent Class
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_user_details(self):
        print("Personal Details:")
        print("")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)


# obj = User("John", 21, "Male")
# obj.show_user_details()

# Child Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    # obj = Bank("Bob", 21, "Male")
    # obj.show_user_details()

    def deposit(self, amount):
        self.balance += amount
        print("Account Balance has been updated: ", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient funds | Balance Available : ", self.balance)
        else:
            self.balance -= self.amount
            print("Account Balance has been updated: ", self.balance)

    # obj = Bank("John", "25", "Male")
    # obj.deposit(500)
    # obj.withdraw(100)
    # obj.withdraw(1000)
    def view_balance(self):
        self.show_user_details()
        print("Account Balance: ", self.balance)
