class Category:

  def __init__(self, name):
    self.ledger = []
    self.name = name

  def deposit(self, amount, desc=""):
    self.ledger.append({"amount": amount, "description": desc})

  def withdraw(self, amount, desc=""):
    if not self.check_funds(amount):
      return False
    else:
      self.ledger.append({"amount": -amount, "description": desc})
      return True
      
  def get_balance(self):
    bal = 0
    for i in self.ledger:
      bal += i["amount"]
    return bal

  def transfer(self, amount, category):
    if not self.check_funds(amount):
      return False
    else:
      self.withdraw(amount, f"Transfer to {category.name}")
      category.deposit(amount, f"Transfer from {self.name}")
      return True

  def check_funds(self, amount):
    if self.get_balance() < amount:
      return False
    else:
      return True

  def __str__(self):
    print("{:*^30}".format(self.name))
    total = 0
    length = 30
    for i in self.ledger:
      print(i["description"][:23] + "{:>{}}".format(str(i["amount"]), length - len(i["description"][:23])))
      total += i["amount"]
    print("Total: " + str(total))
    return ""
    
def create_spend_chart(categories):
  myStr = "Percentage spent by category\n"
  deposits = {}
  purchases = {}
  spent = {}
  
  for cat in categories:
    deposits[cat.name] = (cat.ledger[0]["amount"])
    purchases[cat.name] = 0
    for i in cat.ledger:
      if i["amount"] < 0:
        purchases[cat.name] += abs(i["amount"])
        
  for key, value in deposits.items():
    spent[key] = round((purchases[key]/value * 100)/10) * 10
  
  for i in range(100, -1, -10):
    myStr += "{:>{}}".format(i, 3) + "| "
    for key in spent.keys():
      myStr += ("o  " if spent[key] >= i else "   ")
    myStr += "\n"
    
  myStr += "    " + "-" * (len(spent)*3 + 1 ) + "\n"
  
  for i in range(max([len(key) for key in spent.keys()])):
    myStr += " " * 5
    for key in spent.keys():
      myStr += (key[i] if i < len(key) else " ") + "  "
    myStr += "\n"
    
  return myStr[:-2]