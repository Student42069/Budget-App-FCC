# Tests fails because of withspacing diferrences

import budget
from budget import create_spend_chart
# from unittest import main

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
buisness = budget.Category("Buisness")
buisness.deposit(10000, "initial")
buisness.withdraw(3000, "insurances")
buisness.withdraw(1000, "hookers")
buisness.transfer(3000, food)
other = budget.Category("other")
other.deposit(10000, "INITIAL")
other.withdraw(3000)


print(food)
print(clothing)
print(auto)
print(buisness)
print(other)

print(create_spend_chart([food, clothing, auto, buisness, other]))

# Run unit tests automatically
# main(module='test_module', exit=False)