import config
import random
employees=["hema","ahmed","ali","ahmed"]
prizes=["iPhone", "Laptop", "Vacation"]
add=input("add a new name:")
employees.append(add)
a=employees[-1]
lucky_number=int(input("enter lucky number:"))
win=random.choice(employees)
prize=random.choice(prizes)
if lucky_number%2==0 and win==a :
    print(f"Congratulations! You have won the grand prize! {config.company_budget:,}")
elif lucky_number%2==0:
    print(f"Congratulations! You have won the grand prize! {config.company_budget/2:,}")
else:
    print("Better luck next time")
print(len(employees))
print(employees)
print(type(employees))