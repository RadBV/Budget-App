class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
        
    
    def __str__(self):
        displayCategory = self.determineHeader() + "\n"
        
        for entry in list(self.ledger):
            displayCategory += self.returnLedgerEntry(entry) + "\n"
            
        displayCategory += "Total: " + format(self.balance, ".2f")
            
        return displayCategory
    
    def checkFunds(self, amount):
        if amount > self.balance:
            return False
        return True
    
    def getBalance(self):
        return self.balance
    
    def deposit(self, amount, description=""):
        print(f"Depositing into {self.name}...")
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount
        print("Deposit Successful!")
        
    def withdraw(self, amount, description=""):
        
        print(f"Withdrawing from {self.name}...")
        if not self.checkFunds(amount):
            print("Declined: Not enough for withdrawal.")
            return False
        
        self.ledger.append({'amount': -amount, 'description': description})
        self.balance -= amount
        print("Withdrawal Successful!")
        return True
    
    def transfer(self, amount, category):
        print(f"Transfering ${amount} from {self.name} to {category.name}...")
        if not self.checkFunds(amount):
            print("Transfer Failed: Not enough for transfer.")
            return False
        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        print("Transfer Successful!")
        return True
       
    
    def determineHeader(self):
        fullAsterisks = int(30 - len(self.name))
        halfAsterisks = "*" * int(fullAsterisks/2)
        
        if fullAsterisks/2 % 2 == 0.5 or fullAsterisks/2 % 2 == 1.5:
            return halfAsterisks + self.name + halfAsterisks + "*"
        else:
            return halfAsterisks + self.name + halfAsterisks 
        
            
    def returnLedgerEntry(self, ledgerEntry):
        joinedDescriptionAndAmount = ledgerEntry['description'][0:23] + format(ledgerEntry['amount'], ".2f")
        spaceBetween = " " * (30 - len(joinedDescriptionAndAmount))
        
        return ledgerEntry['description'][0:23] + spaceBetween + format(ledgerEntry['amount'], ".2f")

def createSpendChart(categories):
    pass


food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)