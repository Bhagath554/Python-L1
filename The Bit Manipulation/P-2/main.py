def odd(n):
    #XOR

    if(n ^ 1 == n +1):
        return True
    else:
        return False

num = int(input("Enter the The number"))

if odd(num):
    print(num,"is Even")

else:
    print(num,"is Odd Number")

