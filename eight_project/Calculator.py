class Calculator:
    def k(self):
        num_1=int(input("num 1 :"))
        num_2=int(input("num 2 :"))
        process=int(input("process\n 1 = + \n 2 = - \n 3 = * \n 4 = / \n:"))
        if process==1:
            return f"The result is {num_1} + {num_2} = {num_1+num_2}"
        elif process==2:
            return f"The result is {num_1} - {num_2} = {num_1-num_2}"
        elif process==3:
            return f"The result is {num_1} * {num_2} = {num_1*num_2}"
        elif process==4:
            if num_2 == 0:
                return "cannot divide by zero"
            return f"The result is {num_1} / {num_2} = {num_1/num_2}"
        else :
            return "Input error"

m=Calculator()
print (m.k())