def print_factors(number):
    print("The Factors of this",number,"are:")
    for i in range(1, number +1):
        if number % i == 0:
           print(i)



number = int(input("Enter a Number to find its Factors:"))
print_factors(number)

