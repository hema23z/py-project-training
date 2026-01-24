name=input("enter your name:")
age=int(input("enter your age:"))
password=input("enter Password:")
password_user="123456"
pi=22/7
if 35>=age>=18:
    print ("Your age is between 18 and 35")
else:
    print("You are outside the age range")
print( 35>=age>=18 and "Your age is between 18 and 35" or "You are outside the age range")
if password==password_user:
    print("You are allowed to enter the company!")
else:
    print ("Access Denied!")
print(f"{name:^20}\n"
      f"Hello {name}, your age is: {age}\n"
      f"{1000000:,}\n"
      f"{pi:.2f}")
a='a' in name
print(a)
print (a is True)

      
