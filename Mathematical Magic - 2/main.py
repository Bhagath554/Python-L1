from math import sqrt 
number = int(input("Enter a Number:"))
print("/n")

if number >1 :

    for i in range(2,int(sqrt(number))+1):

        if (number % i ) == 0:

         print(number,"is not a Prime Number")
         break
    else:
        print(number,"is a Prime Number")

        
