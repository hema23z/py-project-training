product_name=input("enter Product name:")
price=float(input ("enter price $ :"))
quantity= int (input("enter Quantity :"))
total_price= price*quantity
tax=0.15*total_price
total=total_price+tax
r_total=round(total,1)
user_budget=int (input ("How much money do you have?"))
can_buy=user_budget>=r_total
is_essential=(product_name == "milk")or (product_name =="hema")
print(f"Product name:{product_name}\nprice:{price}$\nquantity:{quantity}\ntax:15%\ntotal:{r_total}\ncan buy:{can_buy} ")
