def two(num):
    if (num == 0):
        return 0

    if ((num & (~(num - 1))) == num):
        return 1
    return 0

num = int(input("Enter the Number :"))

if(two(num)):
    print("\nIt is the Power of 2")

else:
    print("\nIt is not The Power of 2")

