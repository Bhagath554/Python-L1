num1 = int(input("Enter Largest Number:"))
num2 = int(input("Enter Smallest Number:"))

while(num2):
    store = num2
    num2 = num1 % num2
    num1 = store

print("Hcf is : ",num1)