# Parent class (baasklass)
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)


# Child class (pangakonto klass, pärineb User-ist)
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Account balance has been updated to £", self.balance)

    def withdraw(self, amount):
        self.amount = amount                    # video järgi salvestatakse ajutiselt siia
        if self.amount > self.balance:
            print("Insufficient funds")
            print("Balance available on £", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated to £", self.balance)

    def view_balance(self):
        self.show_details()
        print("Account balance: £", self.balance)


# Näide / testimine (nagu videos lõpus)
yan = Bank("Johan", 20, "male")

yan.deposit(100)
yan.deposit(400)
yan.withdraw(500)
yan.view_balance()