def reverse(n):
   
    num_bits = n.bit_length()
    
    
    reverseno = 0
    
    
    for i in range(num_bits):
        
        reverseno <<= 1
        
        
        reverseno |= n & 1
        
        
        n >>= 1
    
    return reverseno


number = int(input("Enter a number: "))
reverseno = reverse(number)
print(f"Original number: {number}")
print(f"Reversed bits number: {reverseno}")
