def eight(num):
   
    if num > 0 and (num & (num - 1)) == 0:
        
        while num % 8 == 0:
            num //= 8
        return num == 1
    return False

num = int(input("Enter the Number: "))

if eight(num):
    print("\nIt is the Power of 8")
else:
    print("\nIt is not the Power of 8")

