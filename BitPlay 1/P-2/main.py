def no(number,n):

    if number &(1 <<(n-1)):
        print("\nSET")
    else:
        print("\nNot SET")

number = int(input("Enter Number:"))
n = int(input("Enter Bit Number:"))
no(number,n)