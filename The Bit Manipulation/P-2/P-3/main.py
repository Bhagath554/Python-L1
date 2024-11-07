def bits(n):

    count = 0

    while(n):
        count +=1
        n >>= 1

    return count

num = int(input("Enter a Number:"))

print("Total Bits :",bits(num))
