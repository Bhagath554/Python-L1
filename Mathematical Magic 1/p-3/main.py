def romanto(romaninput):
    roman = {'M':1000,'D':500,'C':100,'L':50,'X':10,'I':1,'V':5}

    resultinteger = 0


    for i in range(0,len(romaninput)-1):
        if roman[romaninput[i]] < roman[romaninput[i+1]]:
            resultinteger -= roman[romaninput[i]]

        else :
             resultinteger += roman[romaninput[i]]

    return resultinteger + roman[romaninput[-1]]


roman = input("Input Roman Numeral :")

print("Integer equivalent : ",romanto(roman))
