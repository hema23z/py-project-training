name =input("enter name :")
salary=float(input("enter basic salary:"))
experience=int (input ("Enter the number of years of experience:"))
annual=int (input("Enter the annual rating out of 100:"))
is_vip=False
bonus=0
if annual>=90:
    bonus=0.20*salary
    
elif annual>=70:
    bonus=0.10*salary
total_salary=salary+bonus
if annual>=95 or experience>=10:
    is_vip=True

print (f"===={name}====\n"
       f"{salary}\n"
       f"{total_salary}\n"
       f"{bonus}\n"
       f"VIP Status:{is_vip}\n")

       
       