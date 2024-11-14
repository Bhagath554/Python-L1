def odd(arr,size):
    xorof2 = arr[0]

    x=0
    y=0

    Setbit = 0

    for i in range(1,size):
        xorof2 = xorof2 ^ arr[i]
    
    setbit = xorof2 & ~(xorof2-1)

#x else y
    for i in range(size):
        if(arr[i] & setbit):
            x = x ^ arr[i]
        
        else:
            y = y ^ arr[i]

    print("The Two Odd Elements are :",x,"&",y)

#Create an empty array

arr = []

arr_size = int(input("Enter the size of the Array :"))

for i in range(0,arr_size):
    z = int(input("Enter the number:"))

    arr.append(z)

odd(arr,arr_size)