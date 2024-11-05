
binary_input = input("Enter a binary number: ")


decimal = int(binary_input, 2)


print(f"The decimal equivalent is: {decimal}")
try:
    
    binary_input = input("Enter a binary number: ")
    
   
    decimal = int(binary_input, 2)
    
    
    print(f"The decimal equivalent is: {decimal}")
except ValueError:
    print("Invalid binary number!")

