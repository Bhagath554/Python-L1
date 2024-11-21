def divide(dividend,divisor):
    sign =  (-1 if((dividend < 0) ^
                (divisor < 0))else 1);
    
    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    tempNumb = 0

    for i in range(31,-1,-1):
        if (tempNumb + (divisor << i) <= dividend):
            tempNumb += divisor << i
            quotient |= 1 << i
            print(quotient,tempNumb)

    if sign ==-1:
        quotient = -quotient
    return quotient


a = int(input("Enter Num1 :"))
b = int(input("Enter Num2 "))
print("Result of ",a,"/",b,"is",divide(a,b))