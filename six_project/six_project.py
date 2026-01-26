def show_header():
    print("✦"*20)
def calculate_area(length,width):
    return length*width
def check_even_odd(num):
    if num%2==0:
        return f"the num even:{num}"
    else:
        return f"the num odd:{num}"
def power(exp,base):
    return exp**base
show_header()
length=float (input ("Enter the length:"))
width=float (input ("Enter the width:"))
print (f"the Area=>{calculate_area(length,width)}")
print (power(5,3))
show_header() n