def add(a,b,c):
    return a+b+c

def multiply(a,b,c):
    return a*b*c

def subtract(a,b):
    return a-b
def divide(b,c):
    return b%c
def bodmas(a,b,c):
    return a%b*c+(c-a)

num1 = int(input('Enter number 1'))
num2 = int(input('Enter number 2'))
num3 = int(input('Enter number 3'))

print("sum :",add(num1,num2,num3))
print("Difference :",subtract(num1,num2))
print("Product :",multiply(num1,num2,num3))
print("quotient :",divide(num2,num3))
print("Bodmas :",bodmas(num1,num2,num3))
    