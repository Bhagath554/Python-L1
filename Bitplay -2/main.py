def check(num1,num2):
 
 if ((num1 ^ num2 ) !=0):
    print("Both the Numbers are not equal")

 else:
    print("Both the Numbers are equal")

num1 = int(input("Enter the First Number:"))
num2 = int(input("Enter the Second Number:"))

check(num1,num2)
