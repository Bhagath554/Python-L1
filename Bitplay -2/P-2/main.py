def odd(arr):

    res = 0

    for element in arr:
        res = res ^ element

    return res

arr= []


n = int(input("Enter array Size:"))

while(n):
    num = int(input("Enter number:"))

    arr.append(num)

    n-=1
print("\nODD Occuring Number is :",odd(arr))