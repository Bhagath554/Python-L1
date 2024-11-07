num1 = int(input("Enter Num1:"))
num2 = int(input("Enter Num2:"))

print("num1 & num2 :",num1 & num2)

print("\nnum1 | num2:",num1 | num2)

print("\n~num2:",num2)

print("\nnum1 ^ num2:",num1 ^ num2)

print("\nnum1 << 2:",num1 <<2)

print("\nnum2 <<1",num2 << 1)

def bit(n):
    count = 0
    while(n):
        count +=1
        n >>= 1

    return count

print("Total Bits:",num1)

def odd(n):


    if(n ^ 1 == n +1):
        return True
    else:
        return False

if odd(num2):
    print(num2,"is Even")

else:
    print(num2,"is Odd Number")



