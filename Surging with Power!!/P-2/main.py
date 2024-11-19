def four(num):
    count = 0

    if (num & (~(num & (num -1)))):

        while (num >1):
            num >>= 1
            count += 1

        if (count % 2 == 0):
             return True
        else :
            return False
num = int(input("Enter the Number :"))

if(four(num)):
    print("\nIt is the Power of 4")

else:
    print("\nIt is not The Power of 4")           


