student_marks=[10,80,90,70,40,66,85,57,69,99]
class_info=["hema","ahmed","ali"]
start_n=0
high_n=0
for k in student_marks:
    start_n=start_n+k
    
for hi_n in student_marks:
    if hi_n>high_n:
        high_n=hi_n
        
for n in range(20,0,-2):
    print(n)
    
pasw=input("enter your password:")
if "o"==pasw[-1]:
    print ("welcam")
else:
    print ("incorrect password")
for n in class_info:
    print(n[0])

average=start_n/len(student_marks)
print (high_n)
print (start_n)
print(average)






