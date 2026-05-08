class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
        
    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount
        
    def withdraw(self, amount, description=""):
        print("Attempting to withdraw...")
        if self.balance - amount < 0:
            print("Declined: Not enough for withdrawal.")
            return False
        self.ledger.append({'amount': -amount, 'description': description})
        self.balance -= amount
        print("Withdrawal successful!")
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