class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
        
    def deposit(self, amount, description=""):
        print(f"Depositing into {self.name}...")
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount
        print("Deposit Successful!")
        
    def withdraw(self, amount, description=""):
        print(f"Withdrawing from {self.name}...")
        if self.balance - amount < 0:
            print("Declined: Not enough for withdrawal.")
            return False
        self.ledger.append({'amount': -amount, 'description': description})
        self.balance -= amount
        print("Withdrawal Successful!")
        return True
    
    def transfer(self, amount, category):
        print(f"Transfering ${amount} from {self.name} to {category.name}...")
        if self.balance - amount < 0:
            print("Transfer Failed: Not enough for transfer.")
            return False
        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        print("Transfer Successful!")
        return True
    
    def getBalance(self):
        return f"Current Balance: ${self.balance}"

def createSpendChart(categories):
    pass


food = Category("Food")
food.deposit(900,"deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
print(food.balance)
food.withdraw(1000, "Sushi")

games = Category("Games")
games.deposit(10000, "deposit")
games.transfer(500, food)