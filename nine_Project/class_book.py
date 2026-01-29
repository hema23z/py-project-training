class Book:
    def __init__(self,address,author,number,price):
        self.address=address
        self.author=author
        self.number=number
        self.price=price
    def get_description(self):
        return f"Book title  : {self.address}\nauthor name : {self.author}"
    def apply_discount(self,percentage):
         if percentage>0.5:
            return f"The discount is very large!"
         else:
            self.discount=self.price*percentage
            self.total=self.price-self.discount
            return self.total
        
      
    
    def is_thick(self):
        if self.number >=300:
            return True
        else:
            return False
        
m1=Book("Python 101","hema",500,10)

print(m1.get_description())
print(m1.apply_discount(0.60))
print (m1.is_thick())

