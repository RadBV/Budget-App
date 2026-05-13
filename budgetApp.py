class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
        
    
    def checkFunds(self, amount):
        if amount > self.balance:
            return False
        return True
    
    def getBalance(self):
        return self.balance
    
    def deposit(self, amount, description=""):
        print(f"Depositing into {self.name}...")
        self.ledger.append({'amount': format(amount, ".2f"), 'description': description})
        self.balance += amount
        print("Deposit Successful!")
        
    def withdraw(self, amount, description=""):
        print(f"Withdrawing from {self.name}...")
        if not self.checkFunds(amount):
            print("Declined: Not enough for withdrawal.")
            return False
        self.ledger.append({'amount': format(-amount,".2f"), 'description': description})
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
        
    
    def displayCategory(self):
        header = self.determineHeader()
        print(header)
        
        for entry in list(self.ledger):
            self.printLedgerEntry(entry)
            
        print("Total: " + format(self.balance, ".2f"))
    
    def determineHeader(self):
        fullAsterisks = int(30 - len(self.name))
        halfAsterisks = "*" * int(fullAsterisks/2)
        
        if fullAsterisks/2 % 2 == 0.5 or fullAsterisks/2 % 2 == 1.5:
            return halfAsterisks + self.name + halfAsterisks + "*"
        else:
            return halfAsterisks + self.name + halfAsterisks 
        
            
    def printLedgerEntry(self, ledgerEntry):
        joinedDescriptionAndAmount = ledgerEntry['description'][0:22] + ledgerEntry['amount']
        spaceBetween = " " * (30 - len(joinedDescriptionAndAmount))
        
        print(ledgerEntry['description'][0:22] + spaceBetween + ledgerEntry['amount'])
        return

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

food.displayCategory()
games.displayCategory()