number = int(input("Enter a Number"))


digits =len(str(number))


resultnumber =0
temp = number
while temp > 0:
   digit = temp %10
   resultnumber += digit ** digits
   temp //=10

if number == resultnumber:
    print(number,"is An Armstrong number")

else:
        print(number,"is Not an armstrong number")