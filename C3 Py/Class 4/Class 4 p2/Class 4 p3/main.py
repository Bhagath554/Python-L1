sumofN_no =sum(range(1,11))
print({sumofN_no})

num = int(input("Enter a Number"))
if num > 1 :
    for i in range(+1):

        if num % i==0:
         print(f"{num} is not a prime no.")
         break

        else :
           print(f"{num} is a prime no.")

else :
   print(f"{num} is  not a prime no.")
